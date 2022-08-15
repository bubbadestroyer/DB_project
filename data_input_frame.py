from database import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class DataInputFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()

    def get_data(self):
        amount = self.amount_label_value.get()
        date = self.date_label_value.get()
        date = f'{date[6:10]}-{date[3:5]}-{date[:2]}'
        category_id = self.category_label_value.get()
        if insert_data(
                self.master.table_name, amount, date,
                get_categories_from_category(category_id,
                                             self.master.table_name)):
            self.master.refresh()

    def put_widges(self):
        self.amount_label_text = ttk.Label(self,
                                           text='Сумма',
                                           font=self.master.font)
        self.amount_label_value = ttk.Entry(self, justify=tk.RIGHT)
        self.date_label_text = ttk.Label(self,
                                         text='Дата',
                                         font=self.master.font)
        self.date_label_value = DateEntry(self)
        self.category_label_text = ttk.Label(self,
                                             text='Категория',
                                             font=self.master.font)
        self.category_label_value = ttk.Combobox(self,
                                                 state='readonly',
                                                 values=get_categories(
                                                     self.master.table_name))
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