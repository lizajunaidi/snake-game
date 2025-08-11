import tkinter
import random

ROWS = 25
COLS = 25
SQUARE_SIZE = 25

BOARD_WIDTH = SQUARE_SIZE * ROWS
BOARD_HEIGHT = SQUARE_SIZE * COLS

#game window
window = tkinter
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = BOARD_WIDTH, height = BOARD_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#center window
board_width = window.winfo_width()
board_height = window.winfo_height()
sreen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.mainloop()
