import tkinter as tk
from tkinter import Button, ttk
from unicodedata import category
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
        self.table_frame = StatFrame(self).place(x=300, y=0)

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()


class StatFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()
        
    def put_widges(self):
        self.sum_amount_text = ttk.Label(self, text='Сумма')
        self.sum_amount_value = ttk.Label(self, text=get_sum_amount())

        self.sum_amount_text.grid(row=0,
                                    column=0,
                                    sticky='w',
                                    cnf=self.master.conf)
        self.sum_amount_value.grid(row=0,
                                    column=1,
                                    sticky='e',
                                    cnf=self.master.conf)


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
            table.insert('', tk.END, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


class DataFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()

    def get_data(self):
        amount = self.amount_label_value.get()
        date = self.date_label_value.get()
        date = f'{date[6:10]}-{date[3:5]}-{date[:2]}'
        category_id = self.category_label_value.get()
        if insert_data(amount, date,
                       get_categories_from_category(category_id)):
            self.master.refresh()

    def put_widges(self):
        self.amount_label_text = ttk.Label(self, text='Сумма')
        self.amount_label_value = ttk.Entry(self, justify=tk.RIGHT)
        self.date_label_text = ttk.Label(self, text='Дата')
        self.date_label_value = DateEntry(self)
        self.category_label_text = ttk.Label(self, text='Категория')
        self.category_label_value = ttk.Combobox(self, values=get_categories())
        self.btn_send = ttk.Button(self,
                                   text='Отправить',
                                   command=self.get_data)

        self.amount_label_text.grid(row=0,
                                    column=0,
                                    sticky='w',
                                    cnf=self.master.conf)
        self.amount_label_value.grid(row=0,
                                     column=1,
                                     sticky='e',
                                     cnf=self.master.conf)
        self.date_label_text.grid(row=1,
                                  column=0,
                                  sticky='w',
                                  cnf=self.master.conf)
        self.date_label_value.grid(row=1,
                                   column=1,
                                   sticky='e',
                                   cnf=self.master.conf)
        self.category_label_text.grid(row=2,
                                      column=0,
                                      sticky='w',
                                      cnf=self.master.conf)
        self.category_label_value.grid(row=2,
                                       column=1,
                                       sticky='e',
                                       cnf=self.master.conf)
        self.btn_send.grid(row=3,
                           column=0,
                           columnspan=2,
                           sticky='n',
                           cnf=self.master.conf)


app = App()
app.mainloop()
