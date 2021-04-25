import tkinter
import pandas
import random

data = pandas.read_csv("./data/french_words.csv")


def flip():
    canvas.itemconfig(title, text="English", fill="#FFFFFF")
    canvas.itemconfig(word, text=english_list[french_list.index(random_word)], fill="#FFFFFF")
    canvas.itemconfig(image, image=card_back)
    window.after_cancel(flipper)


def change_word():
    canvas.itemconfig(title, text="French", fill="#000000")
    canvas.itemconfig(image, image=card_front)
    global random_word
    random_word = random.choice(data["French"])
    canvas.itemconfig(word, text=random_word, fill="#000000")
    global flipper
    flipper = window.after(3000, func=flip)


def is_right():
    english_list.remove(english_list[french_list.index(random_word)])
    french_list.remove(random_word)

    new_dict = {french_list[n]: english_list[n] for n in range(0, len(french_list))}

    new_data = pandas.DataFrame(new_dict)
    new_data.to_csv("./data/words_to_learn.csv")
    print("Successfully converted to CSV.")
    change_word()


window = tkinter.Tk()
window.title("Flashy")
window.config(bg="#B1DDC6", padx=50, pady=50)

flipper = window.after(3000, func=flip)

canvas = tkinter.Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
french_list = data["French"].to_list()
english_list = data["English"].to_list()
random_word = random.choice(french_list)
word = canvas.create_text(400, 263, text=random_word, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

image1 = tkinter.PhotoImage(file="./images/wrong.png")
wrong = tkinter.Button(image=image1, highlightthickness=0, bd=0, command=change_word)
wrong.grid(column=0, row=1)

image2 = tkinter.PhotoImage(file="./images/right.png")
right = tkinter.Button(image=image2, highlightthickness=0, bd=0, command=is_right)
right.grid(column=1, row=1)

window.mainloop()
