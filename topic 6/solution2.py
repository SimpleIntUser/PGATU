"""График y = sin(x) с цветными осями и подписью автора."""
import math
import matplotlib.pyplot as plt

AUTHOR = "Вешняков Евгений"


x_values = [-2 * math.pi + 4 * math.pi * i / 1000 for i in range(1001)]
y_values = [math.sin(x) for x in x_values]
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_values, y_values, color="green", label="y = sin(x)")
ax.axhline(0, color="red", linewidth=1.5)
ax.axvline(0, color="blue", linewidth=1.5)
ax.set_title("График функции y = sin(x)")
ax.set_xlabel("X", color="red")
ax.set_ylabel("Y", color="blue")
ax.set_xticks([k * math.pi / 2 for k in range(-4, 5)])
ax.set_xticklabels([f"{k / 2:g}π" if k else "0" for k in range(-4, 5)])
ax.grid(True, alpha=0.3)
ax.legend()
fig.text(0.5, 0.02, f"Автор: {AUTHOR}", ha="center")
fig.tight_layout(rect=(0, 0.05, 1, 1))
plt.show()
