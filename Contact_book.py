from tkinter import *
from tkinter import messagebox, simpledialog
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:  # Check if the name and phone are not empty
        contact_info = f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}"
        task_listbox.insert(END, contact_info)
        
        for entry in [name_entry, phone_entry, email_entry, address_entry]:
            entry.delete(0, END)
        
def delete_contact():
    selected_contact = task_listbox.curselection()
    if selected_contact:
        task_listbox.delete(selected_contact)
        
def update_contact():
    selected_contact = task_listbox.curselection()
    if selected_contact:
        updated_name = name_entry.get()
        updated_phone = phone_entry.get()
        updated_email = email_entry.get()
        updated_address = address_entry.get()
            
        if updated_name and updated_phone:
            updated_contact_info = f"Name: {updated_name}, Phone: {updated_phone}, Email: {updated_email}, Address: {updated_address}"
            task_listbox.delete(selected_contact)
            task_listbox.insert(selected_contact, updated_contact_info)
            for entry in [name_entry, phone_entry, email_entry, address_entry]:
                entry.delete(0, END)
        
def view_contact():
    selected_contact = task_listbox.curselection()
    if selected_contact:
        contact_info = task_listbox.get(selected_contact)
        messagebox.showinfo("Contact Information", contact_info)

def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name to search:")
    if search_term:
        matching_contacts = [contact for contact in task_listbox.get(0, END)]
        if matching_contacts:
            messagebox.showinfo("Search Results", "\n".join(matching_contacts))
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

root = Tk()
root.geometry("420x420")
root.title("Contact Book")


# Labels
name_label = Label(root, text="Name:", font=("Times New Roman", 12))
name_label.place(x=10, y=10)

phone_label = Label(root, text="Phone:", font=("Times New Roman", 12))
phone_label.place(x=10, y=40)

email_label = Label(root, text="Email:", font=("Times New Roman", 12))
email_label.place(x=10, y=70)

address_label = Label(root, text="Address:", font=("Times New Roman", 12))
address_label.place(x=10, y=100)

# Entry widgets for input
name_entry = Entry(root, font=("Times New Roman", 12))
name_entry.place(x=70, y=10)

phone_entry = Entry(root, font=("Times New Roman", 12))
phone_entry.place(x=70, y=40)

email_entry = Entry(root, font=("Times New Roman", 12))
email_entry.place(x=70, y=70)

address_entry = Entry(root, font=("Times New Roman", 12))
address_entry.place(x=70, y=100)
# Buttons
add_button = Button(root, text="Add", font=("Times New Roman", 13), width=8, command=add_contact)
add_button.place(x=10, y=168)

delete_button = Button(root, text="Delete", font=("Times New Roman", 13), width=8, command=delete_contact)
delete_button.place(x=10, y=208)

update_button = Button(root, text="Update", font=("Times New Roman", 13), width=8, command=update_contact)
update_button.place(x=10, y=248)

view_button = Button(root, text="View", font=("Times New Roman", 13), width=8, command=view_contact)
view_button.place(x=10, y=288)

search_button = Button(root, text="Search", font=("Times New Roman", 13), width=8, command=search_contact)
search_button.place(x=10, y=328)


task_listbox = Listbox(root, font=("Times New Roman", 12), width=35, height=10)
task_listbox.place(x=120, y=160)

scrollbar = Scrollbar(root, orient=VERTICAL, command=task_listbox.yview)
# scrollbar.config(command=task_listbox.yview)
scrollbar.place(x=386, y=162, height=200)
task_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
