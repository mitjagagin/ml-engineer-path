# lesson_01_variables.py | Дмитрий Гагин | Переменные, типы данных, f-строки

answer: int = 42 # ответ
floor: int = 9 # этаж
pi: float = 3.14 # число Пи
name: str = "Дмитрий" # имя
is_ml_engineer: bool = True # занимает ли должность

if __name__ == "__main__":
    print(f"Ответ: {answer}") # печатаем ответ
    print(f"Этаж: {floor}") # печатаем этаж
    print(f"Число Пи: {pi}") # печатаем Пи
    print(f"Имя: {name}") # печатаем имя
    print(f"Является AI/ML инженером?: {is_ml_engineer}") # выводим является ли AI/ML инженером