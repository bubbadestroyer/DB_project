import tkinter as tk
from tkinter import ttk
from database import *


class StatFrame(tk.Frame):

    def __init__(self, parent, table_name=None, category=None, flag=None):
        super().__init__(parent)
        self.table_name = table_name
        self.category = category
        self.flag = flag
        self.put_widges()

    def put_widges(self):
        if self.master.table_name == 'costs':
            self.sum_amount_text = ttk.Label(self,
                                             text='Общие расходы',
                                             font=self.master.font)
            self.avg_amount_text = ttk.Label(self,
                                             text='Средняя сумма расходов',
                                             font=self.master.font)
        else:
            self.sum_amount_text = ttk.Label(self,
                                             text='Общие доходы',
                                             font=self.master.font)
            self.avg_amount_text = ttk.Label(self,
                                             text='Средняя сумма доходов',
                                             font=self.master.font)
        self.most_popular_category_text = ttk.Label(
            self, text='Самая популярная категория', font=self.master.font)

        self.sum_amount_text.grid(row=0,
                                  column=0,
                                  sticky='w',
                                  cnf=self.master.conf)
        self.avg_amount_text.grid(row=1,
                                  column=0,
                                  sticky='w',
                                  cnf=self.master.conf)
        self.most_popular_category_text.grid(row=2,
                                             column=0,
                                             sticky='w',
                                             cnf=self.master.conf)
        result = get_sum_avg_amount(self.master.table_name, self.flag,
                                    self.category)
        if result == None:
            pass
        else:
            self.sum_amount_value = ttk.Label(self,
                                            text=result[0][0],
                                            font=self.master.font)
            self.avg_amount_value = ttk.Label(self,
                                            text=result[1][0],
                                            font=self.master.font)
            if self.flag == None:
                self.most_popular_category_value = ttk.Label(self,
                                                            text=get_most_popular_category(self.master.table_name),
                                                            font=self.master.font)
                self.most_popular_category_value.grid(row=2,
                                              column=1,
                                              sticky='e',
                                              cnf=self.master.conf)

        self.sum_amount_value.grid(row=0,
                                   column=1,
                                   sticky='e',
                                   cnf=self.master.conf)
        self.avg_amount_value.grid(row=1,
                                   column=1,
                                   sticky='e',
                                   cnf=self.master.conf)
