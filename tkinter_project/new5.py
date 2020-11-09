from tkinter import *
from tkinter import ttk

master = Tk()
tree=ttk.Treeview(master)
tree["columns"]=("one","two","three")
tree.column("#0", width=100, stretch=NO)
tree.column("one", width=100, stretch=NO)
tree.column("two", width=100,stretch=NO)
tree.column("three", width=100, stretch=NO)
tree.heading("#0",text="Name",anchor=W)
tree.heading("one", text="Date modified",anchor=W)
tree.heading("two", text="Type",anchor=W)
tree.heading("three", text="Size",anchor=W)

tree.pack(side=TOP,fill=X)

master.mainloop()