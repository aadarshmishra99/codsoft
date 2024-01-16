from ast import Import
from tkinter import *
import pickle



def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        list_box.insert(END, task)
        task_entry.delete(0, END)

def remove_task():
    selected_item = list_box.curselection()
    if selected_item:
        list_box.delete(selected_item)
        for item in todo_list:
            list_box.delete(END, item)

def mark_done():
    selected_item = list_box.curselection()
    if selected_item:
        item = list_box.get(selected_item)
        if item.startswitch('√'):
            list_box.itemconfig(selected_item,fg = "black")
            list_box.delete(selected_item)
            list_box.insert(END, item[1:])

        else:
            list_box.itemconfig(selected_item,fg = "black")
            list_box.delete(selected_item)
            list_box.insert(END, '√'+ item)

def save_task():
    with open('todo_list.pkl','wb') as f:
        pickle.dump(todo_list, f)

def load_task():
    try:
        with open('todo_list.pkl','rb') as f:
            todo_list = pickle.loads(f.read())
    except FileNotFoundError:
        todo_list = []

    for item in todo_list:
        list_box.insert(END, item)





app = Tk()
app.title("To-Do List")
app.geometry("720x480")
app.resizable(False,False)
app.config(bg="#242424")
todo_list = []

title = Label(app,text="To-Do Lost",font=("Consolas",18),bg="#242424",fg="#fff")
title.pack(pady=20)

text = StringVar()
task_entry = Entry(app,width=34,textvariable=text,font=("Consolas",12))
task_entry.pack()

add = Button(app,text="Add",width=5,font=("Consolas",12),command=add_task)
add.place(x = 205,y = 110)

remove = Button(app,text="Remove",width=6,font=("Consolas",12),command=remove_task)
remove.place(x = 450,y = 110)

mark = Button(app,text="Mark",width=12,font=("Consolas",12),command=mark_done)
mark.place(x = 300,y = 110)

save = Button(app,text="Save",width=5,font=("Consolas",12),command=save_task)
save.place(x = 205,y = 150)

load = Button(app,text="Load",width=6,font=("Consolas",12),command=load_task)
load.place(x = 450,y = 150)

list_box = Listbox(app,height=15,width=45,font=("Consolas",12))
list_box.place(x = 170, y = 200)

app.mainloop()

#THANKYOU CODESOFT