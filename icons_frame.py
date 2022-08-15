import tkinter as tk
import matplotlib.pyplot as plt
from database import *
from search_frame import SearchFrame


class IconsFrame(tk.Frame):

    def __init__(self, parent, table_frame):
        super().__init__(parent)
        self.table_frame = table_frame
        self.put_widges()

    def put_widges(self):
        self.frame = tk.Frame(self, bd=2)
        self.frame.pack(side=tk.TOP, fill=tk.X)

        self.search_img = tk.PhotoImage(file='./images/search.gif')
        btn_search = tk.Button(self.frame,
                               text='Трата по категории',
                               compound=tk.TOP,
                               image=self.search_img,
                               bd=0,
                               command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='./images/delete.gif')
        btn_delete_value = tk.Button(self.frame,
                                     text='Удалить значение',
                                     compound=tk.TOP,
                                     image=self.delete_img,
                                     bd=0,
                                     command=self.delete_value)
        btn_delete_value.pack(side=tk.LEFT)

        self.diagram_img = tk.PhotoImage(file='./images/diagramma.gif')
        btn_diagram = tk.Button(self.frame,
                                text='Отобразить диаграммой',
                                compound=tk.TOP,
                                image=self.diagram_img,
                                bd=0,
                                command=self.create_diagram)
        btn_diagram.pack(side=tk.LEFT)
        
        self.refresh_img = tk.PhotoImage(file='./images/refresh.gif')
        btn_refresh = tk.Button(self.frame,
                                text='Обновить таблицу',
                                compound=tk.TOP,
                                image=self.refresh_img,
                                bd=0,
                                command=self.master.refresh)
        btn_refresh.pack(side=tk.LEFT)

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
        a = SearchFrame(self, self.master.table_name)
        a.grab_set()