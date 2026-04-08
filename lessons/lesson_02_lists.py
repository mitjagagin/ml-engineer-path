# Урок 2: Списки, цикл for
# Автор: Дмитрий Гагин
# Цель: Изучить что такое списки и для чего они нужны. Цикл for и его применение.

students: list[str] = ["Дмитрий", "Тимофей", "Арина"]
students.append("Ольга")

for student in students:
    print(f"Cтудент: {student}")

print(f"Список студентов: {students}")
print(f"Первый студент: {students[0]}")


