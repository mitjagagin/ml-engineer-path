# Проект 1: Простой менеджер задач
# Автор: Дмитрий Гагин
# Цель: Объединение всего что изучили в единое целое

class Task:
    """Класс описывает задачу. Задача имеет название и статус выполнена или нет, а так же метод
    для изменения статуса"""

    def __init__(self, title: str, is_done: bool = False) -> None:
        self.title = title
        self.is_done = is_done

    def complete(self) -> None:
        """Функция отмечает задачу выполненной"""
        self.is_done = True

class TaskManager:
    """Класс описывает менеджер задач. Хранит, добавляет и выводит"""

    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, title: str) -> None:
        """Добавляет задачу в список задач"""
        self.tasks.append(Task(title))

    def show_tasks(self) -> None:
        """Выводит список всех задачь с названием и статусом"""
        for task in self.tasks:
            if task.is_done:
                print(f'Задача "{task.title}" выполнена')
            else:
                print(f'Задача "{task.title}" не выполнена')

manager = TaskManager()
manager.add_task("Выучить Пайтон")
manager.add_task("Сделать проект")
manager.tasks[0].complete()
manager.show_tasks()


