from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = None
card_is_jpn = True

try:
    jp_words_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    jp_words_df = pandas.read_csv("./data/Copy of 3000 common JP words - All.csv")
    jp_words = jp_words_df.to_dict(orient="records")
else:
    jp_words = jp_words_df.to_dict(orient="records")


# --------------------------------------------SAVE PROGRESS--------------------------------------------------- #
def save_progress():
    jp_words.remove(current_card)
    jp_words_df2 = pandas.DataFrame(jp_words)
    jp_words_df2.to_csv("./data/words_to_learn.csv", index=False)
    generate_word()


# --------------------------------------------FLIP CARD------------------------------------------------------- #
def flip_to_back():
    card_canvas.itemconfig(card_image, image=card_back_img)
    card_canvas.itemconfig(title_text, text="English", fill="white")
    card_canvas.itemconfig(kanji_text, text=current_card["English"], fill="white")
    card_canvas.itemconfig(romaji_text, text="")


def flip_to_front():
    card_canvas.itemconfig(card_image, image=card_front_img)
    card_canvas.itemconfig(title_text, text="Japanese", fill="black")
    card_canvas.itemconfig(kanji_text, text=current_card["Japanese"], fill="black")
    card_canvas.itemconfig(romaji_text, text=current_card["Romaji"])


def flip_card():
    global card_is_jpn
    if card_is_jpn:
        flip_to_back()
    else:
        flip_to_front()
    card_is_jpn = not card_is_jpn


# --------------------------------------------RANDOM CARD DRAW------------------------------------------------ #
def generate_word():
    # global timer,
    global current_card, card_is_jpn
    card_is_jpn = True
    # window.after_cancel(timer)
    current_card = random.choice(jp_words)
    flip_to_front()

    # timer = window.after(3000, flip_card)


# --------------------------------------------UI SETUP-------------------------------------------------------- #
window = Tk()
window.title("Japanese Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# timer = window.after(3000, flip_card)

# Flash Card #

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")

# Canvas
card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = card_canvas.create_image(400, 263, image=card_front_img)
card_canvas.grid(row=0, column=0, columnspan=2)

# Texts
title_text = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
kanji_text = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black", width=400)
romaji_text = card_canvas.create_text(400, 350, text="", font=("Ariel", 40, "normal"), fill="black")

# Buttons
wrong_btn = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=generate_word)
wrong_btn.grid(row=2, column=0)

right_btn = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=save_progress)
right_btn.grid(row=2, column=1)

flip_btn = Button(text="Flip Card", highlightbackground=BACKGROUND_COLOR,
                  font=("Ariel", 45, "normal"), command=flip_card)
flip_btn.grid(row=1, column=0, columnspan=2)

# --------------------------------------------RANDOM CARD DRAW 1st CALL--------------------------------------- #
generate_word()

window.mainloop()
