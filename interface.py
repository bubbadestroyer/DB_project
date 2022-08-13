import tkinter as tk
from tkinter import ttk
from database import *
import matplotlib.pyplot as plt
from DataFrame import *
from TableFrame import *
from StatFrame import *


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.init_main()
        self.title('Семеный бюджет')
        self.geometry('400x300')

    def init_main(self):
        toolbar = tk.Frame(bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.income_img = tk.PhotoImage(file="plus.gif")
        btn_open_income_dialog = tk.Button(toolbar,
                                           text='Посмотреть доходы',
                                           command=self.create_income_frame,
                                           bd=0,
                                           compound=tk.TOP,
                                           image=self.income_img)
        btn_open_income_dialog.pack(side=tk.LEFT)

        self.costs_img = tk.PhotoImage(file="minus.gif")
        btn_open_costs_dialog = tk.Button(toolbar,
                                          text='Посмотреть расходы',
                                          command=self.create_costs_frame,
                                          bd=0,
                                          compound=tk.TOP,
                                          image=self.costs_img)
        btn_open_costs_dialog.pack(side=tk.LEFT)

    def create_costs_frame(self):
        flag = 'costs'
        a = MainFrame(self, flag)
        a.grab_set()

    def create_income_frame(self):
        flag = 'income'
        a = MainFrame(self, flag)
        a.grab_set()


class MainFrame(tk.Toplevel):

    def __init__(self, parent, flag):
        super().__init__(parent)
        self.title('Семеный бюджет')
        self.geometry('600x500')
        self.resizable(False, False)
        self.conf = {'padx': (10, 30), 'pady': 10}
        self.font = 'font 8 bold'
        self.table_name = flag
        self.put_frames()

    def put_frames(self):
        self.table_frame = TableFrame(self)
        self.table_frame.place(x=0, y=275)
        self.icons_frame = IconsFrame(self, self.table_frame).place(x=0, y=0)
        self.data_frame = DataFrame(self).place(x=0, y=100)
        self.stat_frame = StatFrame(self).place(x=300, y=100)

    def put_table(self, category):
        self.master.master.table_frame.destroy()
        self.category = category
        self.table_frame = TableFrame(self, self.table_name, self.category)
        self.table_frame.place(x=0, y=275)

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()


class IconsFrame(tk.Frame):

    def __init__(self, parent, table_frame):
        super().__init__(parent)
        self.table_frame = table_frame
        self.put_widges()

    def put_widges(self):
        self.frame = tk.Frame(self, bd=2)
        self.frame.pack(side=tk.TOP, fill=tk.X)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(self.frame,
                               text='Трата по категории',
                               compound=tk.TOP,
                               image=self.search_img,
                               bd=0,
                               command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete_value = tk.Button(self.frame,
                                     text='Удалить значение',
                                     compound=tk.TOP,
                                     image=self.delete_img,
                                     bd=0,
                                     command=self.delete_value)
        btn_delete_value.pack(side=tk.LEFT)

        self.diagram_img = tk.PhotoImage(file='diagramma.gif')
        btn_diagram = tk.Button(self.frame,
                                text='Отобразить диаграммой',
                                compound=tk.TOP,
                                image=self.diagram_img,
                                bd=0,
                                command=self.create_diagram)
        btn_diagram.pack(side=tk.LEFT)

    def create_diagram(self):
        fig = plt.figure(figsize=(7, 3))
        ax = fig.add_subplot()

        value, labels = get_data_for_diagramm(self.master.table_name)
        ax.pie(value, labels=labels, autopct='%1.1f', shadow=True)

        ax.grid()
        plt.show()

    def delete_value(self):
        self.table_frame.delete()
        self.master.refresh()

    def open_search_dialog(self):
        a = Search(self, self.master.table_name)
        a.grab_set()


class Search(tk.Toplevel):

    def __init__(self, parent, table_name):
        super().__init__(parent)
        self.init_search()
        self.table_name = table_name

    def init_search(self):
        self.title('Поиск')
        self.geometry('600x500')
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
        self.category = self.category_combobox.get()
        MainFrame.put_table(self, self.category)
        self.destroy()




app = App()
app.mainloop()
