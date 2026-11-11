import re

with open("document.txt", "r", encoding="utf-8") as file:
    text = file.read()

updated_text, count = re.subn(
    r"\bдождь\b",
    "ливень",
    text
)

with open("document_updated.txt", "w", encoding="utf-8") as file:
    file.write(updated_text)

print(f"Количество заменённых слов: {count}")