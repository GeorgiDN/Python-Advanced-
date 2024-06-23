# tkmacosx for mac

from tkinter import Button, Entry
from project.buying_page import display_products
from project.canvas import root, frame
from project.helpers import clean_screen, get_password_hash
from json import dump, loads

from project.validators import validate_password, check_for_existing_username


def get_users_data():
    info_data = []

    with open('db/users_information.txt', 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))  # string to dictionary

    return info_data


def render_entry():
    register_button = Button(
        root,
        text='Register',
        bg="green",
        fg="white",
        bd=3,
        width=10,
        height=3,
        command=register   # like object. This is reference to register
    )

    login_button = Button(
        root,
        text='Login',
        bg="blue",
        fg="white",
        bd=3,
        width=10,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 318, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First Name:", font=("Arial", 10))
    frame.create_text(100, 100, text="Last Name:", font=("Arial", 10))
    frame.create_text(100, 150, text="Username:", font=("Arial", 10))
    frame.create_text(100, 200, text="Password:", font=("Arial", 10))

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text='Register',
        bg="green",
        fg="white",
        bd=3,
        command=registration
    )

    frame.create_window(200, 250, window=register_button)


def coordinates_for_errors(field):
    errors_coordinates = {
        "First Name": (200, 75),
        "Last Name": (200, 125),
        "Username": (200, 175),
        "Password": (200, 225)
    }
    x, y = errors_coordinates[field]
    return x, y


def checked_registration(info_dict):
    frame.delete("error", "success")

    # Check for empty fields
    for current_field, value in info_dict.items():
        x, y = coordinates_for_errors(current_field)
        if not value.strip():
            frame.create_text(
                x,
                y,
                text=f"{current_field} cannot be empty",
                fill="red",
                tags="error"
            )
            return False

    # Check if username is already taken
    users_data = get_users_data()
    username_is_taken = check_for_existing_username(users_data, info_dict)

    if username_is_taken:
        return False

    # Password validation
    password = info_dict["Password"]
    is_valid_password = validate_password(password)
    if not is_valid_password:
        return False

    frame.create_text(
        200,
        225,
        text=f"Registration successful",
        fill="green",
        tags="success"
    )

    return True


def registration():
    info_fict = {
        "First Name": first_name_box.get(),
        "Last Name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }
    print(info_fict)

    if checked_registration(info_fict):
        with open("db/users_information.txt", "a") as users_file:
            info_fict["Password"] = get_password_hash(info_fict["Password"])
            dump(info_fict, users_file)  # take dictionary and put in text file in right json format
            users_file.write('\n')
            display_products()


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:", font=("Arial", 10))
    frame.create_text(100, 100, text="Password:", font=("Arial", 10))

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(190, 150, window=login_button)


def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(200,
                          123,
                          text="Invalid username or password",
                          fill="red",
                          tags="error")


def check_login():
    print("in")
    users_data = get_users_data()
    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]
        if current_user_username == user_username and current_user_password == user_password:
            return True
    return False


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for el in info:
        if not el.strip():
            login_button['state'] = 'disabled'
            break
    else:
        login_button['state'] = 'normal'


first_name_box = Entry(root, bd=2)
last_name_box = Entry(root, bd=2)
username_box = Entry(root, bd=2)
password_box = Entry(root, bd=2, show="*")

login_button = Button(
    root,
    text='Login',
    bg="blue",
    fg="white",
    bd=3,
    command=logging
)

login_button["state"] = "disabled"

username_box.bind("<KeyRelease>", change_login_button_status)
password_box.bind("<KeyRelease>", change_login_button_status)

# Initial call to render the entry buttons
render_entry()
