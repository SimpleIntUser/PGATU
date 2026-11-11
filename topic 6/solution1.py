"""Построение графика по координатам из текстового файла."""
from pathlib import Path
import matplotlib.pyplot as plt


def read_points(path):
    return [tuple(map(float, line.split("\t")))
            for line in path.read_text(encoding="utf-8").splitlines()]


points = read_points(Path(__file__).with_name("points.txt"))
x_values, y_values = zip(*points)
fig, ax = plt.subplots()
ax.plot(x_values, y_values, marker="o", color="green")
for x, y in points:
    ax.annotate(f"({x:g}; {y:g})", (x, y),
                xytext=(5, 8), textcoords="offset points")
ax.axhline(0, color="red", linewidth=1)
ax.axvline(0, color="blue", linewidth=1)
ax.set_title("Координаты из файла")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True, alpha=0.3)
ax.margins(0.15)
fig.tight_layout()
plt.show()
