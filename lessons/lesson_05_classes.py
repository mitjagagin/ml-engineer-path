# Урок 5: Классы
# Автор: Дмитрий Гагин
# Цель: Изучить что такое классы и зачем они нужны

class Person:
    """Класс описывает человека по имени и возрасту. Выводит приветствие."""

    def __init__(self, name: str, age: int) -> None:
        """Конструктор вызывается при создании объекта."""
        self.name = name
        self.age = age

    def greet(self) -> None:
        """Функция выводит приветствие"""
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

person = Person("Дмитрий", 45)
print(f"{person.name}, {person.age} лет")
person.greet()
