import csv
from datetime import datetime

from FileContent import FileContent


class MyClass:
    def __init__(self):
        self.content = []  # Loo klassisisene tühi list

    def read_file_contents(self, file_path):
        f = open(file_path, 'r', encoding='utf-8')  # Teeme faili objekti
        data = csv.reader(f, delimiter=';', quotechar='"')
        first_line = next(data)[0]
        if first_line == 'User details':
            for _ in range(10):
                next(data)  # Lükkame lugemis järje 10 rida edasi

            self.content.clear()  # Tühjenda list andmetest
            for row in data:
                date = datetime.strptime(row[0], '%d.%m.%Y').date()
                time = datetime.strptime(row[1], '%H:%M').time()
                self.content.append(FileContent(date, time, float(row[2]),
                                                float(row[3]),
                                                float(row[4]), float(row[5]),
                                                float(row[6]), float(row[7])))

    def get_unique_years(self):
        years = []  # Algselt pole ühtegi aastat. Tühi list
        for row in self.content:
            years.append(row.date.year)  # Lisa aasta listi

        unique_years = list(dict.fromkeys(years))  # Ainult unikaalsed aastad
        unique_years.sort()  # Sorteeri kasvavalt A->Z vs 0->9
        return unique_years  # Tagasta unikaaslsed aastad
