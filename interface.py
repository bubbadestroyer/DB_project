import tkinter as tk
from tkinter import ttk
from database import *

window = tk.Tk()
window.title('Семеный бюджет')
window.geometry('600x500')
window.resizable(False, False)

table_list = tk.Frame(window, width=600, height=300)

table_list.place(x=0, y=300)
heads = get_columns_name()
table = ttk.Treeview(table_list, show='headings')
table['columns'] = heads

for header in heads:
    table.heading(header, text=header,anchor='center')
    table.column(header, anchor='center')
    table.column(header, width=150)


print(get_date())
for row in get_date():
    table.insert('', 0, values=row)
    print(row)



table.pack(expand=tk.YES, fill=tk.BOTH)

window.mainloop()