import tkinter as tk
from main_frame import MainFrame
from database import *


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.init_main()
        self.title('Семеный бюджет')
        self.geometry('400x300')

    def init_main(self):
        toolbar = tk.Frame(bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.income_img = tk.PhotoImage(file="./images/plus.gif")
        btn_open_income_dialog = tk.Button(toolbar,
                                           text='Посмотреть доходы',
                                           command=self.create_income_frame,
                                           bd=0,
                                           compound=tk.TOP,
                                           image=self.income_img)
        btn_open_income_dialog.pack(side=tk.LEFT)

        self.costs_img = tk.PhotoImage(file="./images/minus.gif")
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


app = App()
app.mainloop()
