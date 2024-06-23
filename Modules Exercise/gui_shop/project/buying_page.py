from tkinter import Button
from PIL import ImageTk, Image
from helpers import clean_screen
from json import load, dump

# load ot json to dictionary

from project.canvas import frame, root


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products.json", "r") as stock:
        info = load(stock)

    x, y = 150, 70

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))  # open picture
        images.append(item_img)
        # keep reference to the image so that tkinter does not delete after function

        frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 11))
        frame.create_image(x, y + 120, image=item_img)

        if item_info["quantity"] > 0:
            color = "green"
            text = f"In stock: {item_info['quantity']}"
            item_button = Button(
                root,
                text="Buy",
                bg="green",
                fg="white",
                font=("Comic Sans MS", 10),
                width=5,
                command=lambda x=item_name, y=info: buy_product(x, y)
            )

            frame.create_window(x, y + 280, window=item_button)
        else:
            color = "red"
            text = "Out of stock"

        frame.create_text(x, y + 250, text=text, fill=color, font=("Comic Sans MS", 11))

        x += 400
        if x >= 750:
            y += 330
            x = 150


def buy_product(product_name, info):
    info[product_name]["quantity"] -= 1

    with open("db/products.json", "w") as stock:
        dump(info, stock)

    display_products()


images = []
