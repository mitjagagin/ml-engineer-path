# Урок 3: Словари
# Автор: Дмитрий Гагин
# Цель: Изучить что такое словари и для чего они нужны.

from typing import Union

person: dict[str, Union[int, str]] = {
    "name": "Дмитрий",
    "age": 45,
    "height": 185,
    "weight": 90
}

for key, value in person.items():
    print(f"{key}: {value}")

print(f"Имя личности: {person['name']}")
