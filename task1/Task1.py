'''
Task no. 1 : make To-do list
language: Python

'''




from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(END, f"{len(listbox_tasks.get(0, END)) + 1}: {task}")
        entry_task.delete(0, END)
        messagebox.showinfo("Message","Task added successfully!")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, f"{index + 1}: {updated_task}")
            entry_task.delete(0, END)
            messagebox.showinfo("Message","Task updated successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def clear_tasks():
    listbox_tasks.delete(0, END)
    
    
def on_delete_key(event):
    delete_task()

def save_tasks():
    with open("todo_list.txt", "w") as f:
        tasks = listbox_tasks.get(0, END)
        for task in tasks:
            f.write(task + "\n")
def on_enter_key(event):
    add_task()

def load_tasks():
    try:
        with open("todo_list.txt", "r") as f:
            for line in f:
                listbox_tasks.insert(END, line.strip())
    except FileNotFoundError:
        pass

window = Tk()
window.title("To-Do List")
window.configure(bg='light gray')
window.iconbitmap("icon.ico")
window.bind("<Delete>", on_delete_key)
window.minsize(600,600)


style = ttk.Style()
style.configure(
    "Beautiful.TButton",
    font=("Arial", 10,"bold"),
    foreground="black",
    background="black",
    relief=GROOVE,
    borderwidth=2,
    padx=2,
    pady=2
)
style.map("Beautiful.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', 'black'), ('active', 'white')]
    )
img=PhotoImage(file="task1.png")
img_label=Label(window,image=img,text="TO-DO LIST", font=("Ariel",25,"bold","italic"),compound=LEFT,bg="sky blue",height=120)
img_label.pack(fill=BOTH,pady=2)
title_label2=Label(text="ADD ITEM:", font=("Ariel",15,"bold"),bg ="light grey", justify="left")
title_label2.pack(anchor=W,fill=BOTH)

frame_top1 = Frame(window,bg="light grey")
frame_top1.pack()
frame_top = Frame(window,bg="light grey")
frame_top.pack(pady=20)


entry_task = Entry(frame_top1, width=50,background="light grey", font=("Helvetica", 14),border=3)
entry_task.pack(side=LEFT,pady=5,padx=10)
entry_task.focus_set() 
entry_task.bind("<Return>", on_enter_key)  


btn_add_task = ttk.Button(frame_top, text="Add", width=10, command=add_task,style="Beautiful.TButton")
btn_add_task.pack(side=LEFT)
btn_update_task = ttk.Button(frame_top, text="Update", width=10, command=update_task,style="Beautiful.TButton")
btn_update_task.pack(side=LEFT)
btn_delete_task = ttk.Button(frame_top, text="Delete", width=10, command=delete_task,style="Beautiful.TButton")
btn_delete_task.pack(side=LEFT)
btn_clear_tasks = ttk.Button(frame_top, text="Clear", width=10, command=clear_tasks,style="Beautiful.TButton")
btn_clear_tasks.pack(side=LEFT)   
btn_save_tasks = ttk.Button(frame_top, text="Save", width=10, command=save_tasks,style="Beautiful.TButton")
btn_save_tasks.pack(side=LEFT)
btn_load_tasks = ttk.Button(frame_top, text="Load", width=10, command=load_tasks,style="Beautiful.TButton")
btn_load_tasks.pack(side=LEFT)

title_label3=Label(text="***** ITEMS *****", font=("Ariel",15,"bold"),bg ="light grey", justify="left")
title_label3.pack(anchor=W,fill=BOTH)
frame_tasks = Frame(window)
frame_tasks.pack(padx=10)

listbox_tasks = Listbox(frame_tasks, bg='light grey',width=50, height=10, font=("Helvetica", 14,"italic","underline"),selectbackground="sky blue",selectforeground="black")
listbox_tasks.pack(side=LEFT, fill=BOTH)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=BOTH)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

copyright_label =Label(window, text="© 2023 CodSoft. All rights reserved.",
                           font=("Arial", 10), fg="gray")
copyright_label.pack(side=BOTTOM, pady=5,fill=BOTH)

load_tasks()
window.mainloop()
