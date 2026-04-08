# lesson_03_dicts.py | Дмитрий Гагин | Словари, доступ по ключу, итерация .items()

from typing import Union # импорт Union

person: dict[str, Union[int, str]] = { # словарь для хранения личности
    "name": "Дмитрий",
    "age": 45,
    "height": 185,
    "weight": 90
}
if __name__ == "__main__":
    for key, value in person.items(): # в цикле перебтраем ключ -> значение
        print(f"{key}: {value}") # печатаем их

    print(f"Имя личности: {person['name']}") # печатаем значение ключа "name"