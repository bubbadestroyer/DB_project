import tkinter as tk
from tkinter import ttk
from database import *
from tkcalendar import DateEntry
import matplotlib.pyplot as plt


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.init_main()
        self.title('Семеный бюджет')
        self.geometry('400x300')

    def init_main(self):
        toolbar = tk.Frame(bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="minus.gif")
        btn_open_dialog = tk.Button(toolbar,
                                    text='Посмотреть расходы',
                                    command=self.open_dialog,
                                    bd=0,
                                    compound=tk.TOP,
                                    image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        a = CostsFrame(self)
        a.grab_set()


class CostsFrame(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title('Семеный бюджет')
        self.geometry('600x500')
        self.resizable(False, False)
        self.conf = {'padx': (10, 30), 'pady': 10}
        self.font = 'font 10 bold'
        self.table_name = 'costs'
        self.put_frames()

    def put_frames(self):
        self.icons_frame = IconsFrame(self).place(x=0, y=0)
        self.data_frame = DataFrame(self).place(x=0, y=100)
        self.table_frame = TableFrame(self).place(x=0, y=275)
        self.stat_frame = StatFrame(self).place(x=300, y=100)

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()


class IconsFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()

    def put_widges(self):
        self.frame = tk.Frame(self, bd=2)
        self.frame.pack(side=tk.TOP, fill=tk.X)

        self.add_income = tk.PhotoImage(file='diagramma.gif')
        btn_add_income = tk.Button(self.frame,
                                   text='Отобразить диаграммой',
                                   compound=tk.TOP,
                                   image=self.add_income,
                                   bd=0,
                                   command=self.create_diagram)
        btn_add_income.pack(side=tk.LEFT)

    def create_diagram(self):
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot()

        value, labels = get_data_for_diagramm(self.master.table_name)
        ax.pie(value, labels=labels, autopct='%1.1f', shadow=True)

        ax.grid()
        plt.show()


class StatFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.put_widges()

    def put_widges(self):
        self.sum_amount_text = ttk.Label(self,
                                         text='Общие расходы',
                                         font=self.master.font)
        self.sum_amount_value = ttk.Label(self,
                                          text=get_sum_amount(),
                                          font=self.master.font)
        self.most_popular_category_text = ttk.Label(
            self, text='Самая популярная категория', font=self.master.font)
        self.most_popular_category_value = ttk.Label(
            self, text=get_most_popular_category(), font=self.master.font)
        self.avg_amount_text = ttk.Label(self,
                                         text='Средняя сумма расходов',
                                         font=self.master.font)
        self.avg_amount_value = ttk.Label(self,
                                          text=get_avg_amount(),
                                          font=self.master.font)

        self.sum_amount_text.grid(row=0,
                                  column=0,
                                  sticky='w',
                                  cnf=self.master.conf)
        self.sum_amount_value.grid(row=0,
                                   column=1,
                                   sticky='e',
                                   cnf=self.master.conf)
        self.most_popular_category_text.grid(row=2,
                                             column=0,
                                             sticky='w',
                                             cnf=self.master.conf)
        self.most_popular_category_value.grid(row=2,
                                              column=1,
                                              sticky='e',
                                              cnf=self.master.conf)
        self.avg_amount_text.grid(row=1,
                                  column=0,
                                  sticky='w',
                                  cnf=self.master.conf)
        self.avg_amount_value.grid(row=1,
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
            table.column(header, width=145)

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
                                                 values=get_categories(),
                                                 font=self.master.font)
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
