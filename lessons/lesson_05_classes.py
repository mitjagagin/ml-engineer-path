# lesson_05_classes.py | Дмитрий Гагин | Классы, __init__, методы, создание объектов

class Person:
    """Класс описывает человека по имени и возрасту. Выводит приветствие."""

    def __init__(self, name: str, age: int) -> None:
        """Конструктор вызывается при создании объекта."""
        self.name = name # инициализируем name
        self.age = age # инициализируем age

    def greet(self) -> None:
        """Функция выводит приветствие"""
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет") # печатаем приветсвие

if __name__ == "__main__":
    person = Person("Дмитрий", 45) # создаем экземпляр класса Person
    print(f"Имя: {person.name}, возраст: {person.age} лет") # печатаем значения атрибутов экземпляра Person
    person.greet() # вызов метода экземпляра Person