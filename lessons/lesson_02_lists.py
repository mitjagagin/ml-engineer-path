# Урок 2: Списки, цикл for
# Автор: Дмитрий Гагин
# Цель: Изучить что такое списки и для чего они нужны. Цикл for и его применение.

students: list[str] = ["Bob", "John", "Michael"]
students.append("Anna")

for student in students:
    print(student)

print(students)
print(students[0])


