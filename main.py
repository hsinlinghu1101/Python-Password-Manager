from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letter = [choice(letters) for char in range(randint(8, 10))]
    pwd_symbols = [choice(symbols)for char in range(randint(2, 4))]
    pwd_numbers = [choice(numbers)for char in range(randint(2, 4))]

    password_list = pwd_letter + pwd_symbols + pwd_numbers

    shuffle(password_list)

    new_pwd = "".join(password_list)
    input_3.insert(0, new_pwd)
    pyperclip.copy(new_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = input_1.get()
    email = input_2.get()
    pwd = input_3.get()

    new_data = {
        web: {
            "Email": email,
            "Password": pwd
        }
    }

    if web == "" or email == "" or pwd == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}\n"
                                                      f"Password: {pwd} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                input_1.delete(0, END)
                input_3.delete(0, END)

# ---------------------------- FIND PASSWORD------------------------------- #
def find_password():
    web = input_1.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(title=web, message=f"Email: {data[web]['Email']}\nPassword: {data[web]['Password']}")
            else:
                messagebox.showinfo(title="Error", message="No Data Found.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No details for {web} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0, columnspan=2)
website = Label(text="Website:")
website.grid(column=0, row=1)
input_1 = Entry(width=35)
input_1.focus()
input_1.grid(column=1, row=1)
search = Button (text="Search", command=find_password, activebackground="blue")
search.grid(column=2, row=1, sticky="EW" )
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
input_2 = Entry(width=35)
input_2.insert(0, "melody123@gmail.com")
input_2.grid(column=1, row=2, columnspan=2, sticky="EW")
password = Label(text="Password:")
password.grid(column=0, row=3)
input_3 = Entry(width=21)
input_3.grid(column=1, row=3, sticky="EW")
generate = Button(text="Generate Password", command=get_password)
generate.grid(column=2, row=3, sticky="EW")
add = Button(text='Add', width=36, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="EW")
window.mainloop()
