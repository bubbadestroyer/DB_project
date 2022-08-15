from data_frame import DataFrame
from stat_frame import StatFrame
from table_frame import TableFrame
from icons_frame import IconsFrame
import tkinter as tk

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
        self.table = TableFrame(self.master.master, self.table_name, self.category)
        self.table.place(x=0, y=275)

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()