# lesson_02_lists.py | Дмитрий Гагин | Списки, индексы, циклы

students: list[str] = ["Дмитрий", "Тимофей", "Арина"] # список студентов
students.append("Ольга") # добавляем в список

if __name__ == "__main__":
    for student in students: # в цикле
        print(f"Студент: {student}") # выводим студентов

    print(f"Список студентов: {students}") # выводим весь список
    print(f"Первый студент: {students[0]}") # выводим первый элемент