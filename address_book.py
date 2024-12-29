import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

def store_data():
    name = name_entry.get()
    if name == "":
        messagebox.showerror("Error!", "You have not entered anything.")
    else:
        if name not in my_address_book.keys():
            addressbox.insert(tk.END, name)
        
        my_address_book[name] = (address_entry.get(), mobile_entry.get(), email_entry.get(), birthday_entry.get())
        clear_all()

def clear_all():
    name_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    mobile_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    birthday_entry.delete(0,tk.END)

def edit_data():
    clear_all()
    index = addressbox.curselection()
    if index:
        key = addressbox.get(index)
        name_entry.insert(0,key)
        details = my_address_book[key]
        address_entry.insert(0,details[0])
        mobile_entry.insert(0,details[1])
        email_entry.insert(0,details[2])
        birthday_entry.insert(0,details[3])
    else:
        messagebox.showwarning("???","Nothing has been selected.")
    
def delete_data():
    index = addressbox.curselection()
    if index:
        key = addressbox.get(index)
        addressbox.delete(index)
        del my_address_book[key]
    else:
        messagebox.showerror("Error!", "You have not selected anything.")

def save():
    save_file = asksaveasfile(defaultextension=".txt")
    if save_file:
        print(my_address_book, file=save_file)
        reset()
    else:
        messagebox.showerror("Saving Issue", "You canceled the download.")
        
def reset():
    clear_all()
    addressbox.delete(0,tk.END)
    my_address_book.clear()
    
window = tk.Tk()
window.geometry("800x800")
window.title("Address Book")

# Color
bg_main = "#f5f5f5"
bg_top = "#4CAF50"
bg_list = "#FFFFFF"
bg_info = "#E3F2FD"
button_color = "#2196F3"
button_text = "#FFFFFF"
label_color = "#000000"

my_address_book = {}

# Top Frame
top_frame = tk.Frame(window, bg="lightgray", height=50, relief="ridge", borderwidth=2)
top_frame.pack(side=tk.TOP, fill=tk.X)

book_label = tk.Label(top_frame, text="My Address Book", font=("Arial", 20), bg="lightgray")
book_label.pack(padx=10, pady=10, side=tk.LEFT)

open_button = tk.Button(top_frame, text="Open", font=("Arial", 16), width=1)
open_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Left Frame
list_frame = tk.Frame(window, width=300, bg="white", relief="ridge", borderwidth=2)
list_frame.pack(side=tk.LEFT, fill=tk.Y)

addressbox = tk.Listbox(list_frame, font=("Arial", 16), width=20, height=25)
addressbox.pack(padx=10, pady=10)

edit_button = tk.Button(list_frame, text="Edit", font=("Arial", 16), width=10, command=edit_data)
edit_button.pack(padx=5, pady=10)

delete_button = tk.Button(list_frame, text="Delete", font=("Arial", 16), width=10, command=delete_data)
delete_button.pack(padx=5, pady=10)

# Right Frame
info_frame = tk.Frame(window, bg="lightblue", relief="ridge", borderwidth=2)
info_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

name_label = tk.Label(info_frame, text="Full Name: ", font=("Arial", 16), bg="lightblue")
name_label.place(relx=0.05, rely=0.05)

name_entry = tk.Entry(info_frame, font=("Arial", 16), width=30)
name_entry.place(relx=0.35, rely=0.05)

address_label = tk.Label(info_frame, text="Address: ", font=("Arial", 16), bg="lightblue")
address_label.place(relx=0.05, rely=0.15)

address_entry = tk.Entry(info_frame, font=("Arial", 16), width=30)
address_entry.place(relx=0.35, rely=0.15)

mobile_label = tk.Label(info_frame, text="Mobile Number: ", font=("Arial", 16), bg="lightblue")
mobile_label.place(relx=0.05, rely=0.25)

mobile_entry = tk.Entry(info_frame, font=("Arial", 16), width=30)
mobile_entry.place(relx=0.35, rely=0.25)

email_label = tk.Label(info_frame, text="Email: ", font=("Arial", 16), bg="lightblue")
email_label.place(relx=0.05, rely=0.35)

email_entry = tk.Entry(info_frame, font=("Arial", 16), width=30)
email_entry.place(relx=0.35, rely=0.35)

birthday_label = tk.Label(info_frame, text="Date of Birth (YYYY-MM-DD): ", font=("Arial", 16), bg="lightblue")
birthday_label.place(relx=0.05, rely=0.45)

birthday_entry = tk.Entry(info_frame, font=("Arial", 16), width=30)
birthday_entry.place(relx=0.35, rely=0.45)

update_button = tk.Button(info_frame, text="Update/Add", font=("Arial", 16), width=15, command=store_data)
update_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

save_button = tk.Button(window, text="Save", font=("Arial", 16), width=15, command=save)
save_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

window.mainloop()
