import tkinter as tk
from tkinter import ttk
from database import *
from tkcalendar import DateEntry, Calendar


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Семеный бюджет')
        self.geometry('600x500')
        self.resizable(False, False)
        self.conf = {'padx': (10, 30), 'pady': 10}
        self.put_frames()

    def put_frames(self):
        self.data_frame = DataFrame(self).place(x=0, y=0)
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

        for row in get_costs():
            print(row)
            table.insert('', 0, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


class DataFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()

    def put_widges(self):
        self.amount_label_text = ttk.Label(self, text='Сумма')
        self.amount_label_value = ttk.Entry(self, justify=tk.RIGHT)
        self.date_label_text = ttk.Label(self, text='Дата')
        self.date_label_value = DateEntry(self)
        self.category_label_text = ttk.Label(self, text='Категория')
        self.category_label_value = ttk.Combobox(self, values=get_categories())

        self.amount_label_text.grid(row=0, column=0, sticky='w', cnf=self.master.conf)
        self.amount_label_value.grid(row=0, column=1, sticky='e', cnf=self.master.conf)
        self.date_label_text.grid(row=1, column=0, sticky='w', cnf=self.master.conf)
        self.date_label_value.grid(row=1, column=1, sticky='e', cnf=self.master.conf)
        self.category_label_text.grid(row=2, column=0, sticky='w', cnf=self.master.conf)
        self.category_label_value.grid(row=2, column=1, sticky='e', cnf=self.master.conf)


app = App()
app.mainloop()
