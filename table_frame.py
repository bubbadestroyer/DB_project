from database import *
import tkinter as tk
from tkinter import ttk


class TableFrame(tk.Frame):

    def __init__(self, parent, table_name = None, category = None):
        super().__init__(parent)
        self.table_name = table_name
        self.category = category
        self.put_widges()

    def put_widges(self):
        heads = get_columns_name(self.table_name if self.table_name != None else self.master.table_name)
        self.table = ttk.Treeview(self, show='headings')
        self.table['columns'] = heads

        for header in heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center')
            self.table.column(header, width=145)

        for row in get_table(self.master.table_name, self.category):
            self.table.insert('', tk.END, values=row)

        scroll_pane = ttk.Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)

    def delete(self):
        for selection_item in self.table.selection():
            delete_data(self.master.table_name,
                        self.table.set(selection_item, '#1'))