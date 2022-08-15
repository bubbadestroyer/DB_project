import tkinter as tk
from database import *
from tkinter import ttk


class SearchFrame(tk.Toplevel):

    def __init__(self, parent, table_name):
        super().__init__(parent)
        self.init_search()
        self.table_name = table_name

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        self.label_search = tk.Label(self, text='Поиск')
        self.label_search.place(x=50, y=20)

        self.category_combobox = ttk.Combobox(
            self, values=get_categories(self.master.master.table_name))
        self.category_combobox.place(x=105, y=20, width=150)

        self.btn_cancel = ttk.Button(self,
                                     text='Закрыть',
                                     command=self.destroy)
        self.btn_cancel.place(x=185, y=50)

        self.btn_search = ttk.Button(self,
                                     text='Поиск',
                                     command=self.search_data)
        self.btn_search.place(x=105, y=50)

    def search_data(self):
        from main_frame import MainFrame
        self.category = self.category_combobox.get()
        MainFrame.put_table(self, self.category)
        self.destroy()