from tkinter import *
import ctypes
from tkinter import messagebox
import random
import pyperclip
import json
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():  
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password="".join(password_list)
    password_label_entry.insert(0, password)

    pyperclip.copy(password)


    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    email = email_username_entry.get()
    password = password_label_entry.get()
    
    new_data = {
        website: {
            "email":email ,
            "password": password,



        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Wrong!", message="Please make sure you haven't left any fields empty.")
    
    else:
        try:
            with open("data.json","r") as data_file:
                
                #reading old data
                data = json.load(data_file)
                
             
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:
           #updating old data with new_data
            data.update(new_data)
        
        
            with open ("data.json","w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0,END)
            password_label_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
         
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No data file found.")

    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {
                    password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {website} found.")





    

# ---------------------------- UI SETUP ------------------------------- #

#WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#CANVAS
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png") 
canvas.create_image(100,100,image = logo_img)
canvas.grid(column=1,row=0)

#LABEL
website_label = Label(text="Website:",padx=3,pady=3)
email_username = Label(text="Email/Username:",padx=3,pady=3)
password_label = Label(text="Password:",padx=3,pady=3)
#LABEL POSİTİON
website_label.grid(column=0,row=1)
email_username.grid(column=0,row=2)
password_label.grid(column=0,row=3)

#ENTRY
website_entry = Entry(width=35)
email_username_entry = Entry(width=35)
password_label_entry = Entry(width=35)
#ENTRY POSİTİON
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
website_entry.focus()

email_username_entry.grid(column=1,row=2, columnspan=2,sticky="EW")
email_username_entry.insert(0,"odin @gmail.com")

password_label_entry.grid(column=1,row=3,sticky="EW")


#BUTTON
generate_password_button = Button(text="Generate Password",command=generate_password)

add_button = Button(text="Add",width=35,command=save)

search_button = Button(text="Search",command=find_password )

#BUTTON POSİTİON
generate_password_button.grid(column=3,row=3,sticky="EW")
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")
search_button.grid(column=3,row=1,sticky="EW")


















window.mainloop()