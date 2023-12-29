from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("To DO List")
root.geometry("300x400+400+100")
root.config(bg="#2f4f4f")
root.resizable(0,0)

def add_task():
    new_task = entry_box.get()
    if new_task:
        tasks.insert(END, new_task)
        entry_box.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!", message="please enter some task")
        
def delete_task():
    try:
        selected_task_index = tasks.curselection()[0]
        tasks.delete(selected_task_index)
    except:
        tkinter.messagebox.showwarning(title="Attention!!", message="Please select task ")

def update_task():
    
    selected_task_index = tasks.curselection()
    if selected_task_index:
        updated_task = entry_box.get()
        if updated_task == "":
            tkinter.messagebox.showwarning(title="Attention!!", message="please enter some task")
        else:
            tasks.delete(selected_task_index)
            tasks.insert(selected_task_index, updated_task)
            entry_box.delete(0, END)

# frame
frame = Frame(root, bg="#212120", height=50, width=450)
frame.pack(side=TOP)
# Heading label
Label(frame, text='All task', bg='#212120', fg="white", font=("Time New Roman", 15, 'bold'), wraplength=300).place(x=110, y=10)

# todo_Task
tasks = Listbox(root, selectbackground='Gold', bg='white', font=('Helvetica', 12), height=12, width=30)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=270, y=50, height=231)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=15, y=50)

# EntryBox
entry_box = Entry(root,font=("Times New Roman", 10), width=45)
entry_box.place(x=15, y=300, height=25)

# Buttons
add_button = Button(root, text='Add', bg='Azure', width=8, font=('Helvetica', 12), command=add_task)
add_button.place(x=15, y=350)

delete_button = Button(root, text='Delete', bg='Azure', width=8, font=('Helvetica', 12), command=delete_task)
delete_button.place(x=110, y=350)

update_button = Button(root, text='Update', bg='Azure', width=8, font=('Helvetica', 12), command=update_task)
update_button.place(x=208, y=350)

root.mainloop()