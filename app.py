from tkinter import *
from tkinter.ttk import Combobox

win = Tk()
win.geometry('400x350')
win.title('Tervise Statistika')
win.resizable(False, False)

# Frame, kuhu peale tulevad kõik vidinad (Widgets)
frame = Frame(win)
frame.pack(side=TOP, anchor=NW, padx=5, pady=5)

# Nupp (Button) faili avamiseks (rida 1)
btn_open = Button(frame, text='Ava fail')
btn_open.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

# Rippmenüü (Combobox) unikaalsetele aastatele (rida 1)
cmb_years = Combobox(frame)
cmb_years['values'] = ['Vali aasta']  # Mida näidata rippmenüüs
cmb_years.current(0)  # Milline valik on aktiivne rippmenüüs
cmb_years.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

# Nupp (Button) info näitamiseks (rida 1)
btn_show = Button(frame, text='Näita tulemusi')
btn_show.grid(row=0, column=2, sticky=EW, padx=5, pady=5)

# Silt (Label) avatud faili nim enäitamiseks (rida 2).
lbl_file = Label(frame, text='Siia tuleb failinimi')
lbl_file.grid(row=1, column=0, columnspan=3, sticky=W, padx=5, pady=5)

# Mitmerealine tekstikast (Text). TUlemuse näitamiseks (rida 3)
txt_result = Text(frame, width=45, height=14)
txt_result.grid(row=2, column=0, columnspan=3, sticky=W, padx=5, pady=5)

win.mainloop()