"""Построение параболы y = x² средствами Tkinter."""
import tkinter as tk


root = tk.Tk()
root.title("График y = x²")
canvas = tk.Canvas(root, width=700, height=500, bg="white")
canvas.pack()
canvas.create_text(350, 20, text="График функции y = x²", font=("Arial", 16))

for x in range(-5, 6):
    px = 350 + x * 55
    canvas.create_line(px, 50, px, 440, fill="#eeeeee")
    canvas.create_text(px, 455, text=str(x))
for y in range(5, 26, 5):
    py = 440 - y * 15
    canvas.create_line(60, py, 640, py, fill="#eeeeee")
    canvas.create_text(330, py, text=str(y))
canvas.create_line(50, 440, 650, 440, arrow=tk.LAST, fill="red", width=2)
canvas.create_line(350, 460, 350, 40, arrow=tk.LAST, fill="blue", width=2)
canvas.create_text(665, 440, text="X")
canvas.create_text(350, 30, text="Y")
curve = []
for i in range(501):
    x = -5 + i / 50
    curve.extend((350 + x * 55, 440 - x ** 2 * 15))
canvas.create_line(*curve, fill="purple", width=2)
root.mainloop()
