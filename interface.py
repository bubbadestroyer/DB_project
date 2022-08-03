import tkinter as tk
from tkinter import ttk
from database import *


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Семеный бюджет')
        self.geometry('600x500')
        self.resizable(False, False)
        self.put_frames()

    def put_frames(self):
        self.table_frame = TableFrame(self).place(x=0, y=300)


class TableFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()

    def put_widges(self):
        heads = get_columns_name()
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
            table.column(header, width=150)

        for row in get_date():
            print(row)
            table.insert('', 0, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


app = App()
app.mainloop()
