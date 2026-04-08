# task_manager.py | Дмитрий Гагин | Менеджер задач (CLI), классы и методы

class Task:
    """Класс описывает задачу. Задача имеет название и статус выполнена или нет, а так же метод
    для изменения статуса"""

    def __init__(self, title: str, is_done: bool = False) -> None:
        self.title = title # инициализация title
        self.is_done = is_done # инициализация is_done

    def complete(self) -> None:
        """Функция отмечает задачу выполненной"""
        self.is_done = True # помечаем задачу выполненной

class TaskManager:
    """Класс описывает менеджер задач. Хранит, добавляет и выводит"""

    def __init__(self) -> None:
        self.tasks: list[Task] = [] # создаем пустой список задач

    def add_task(self, title: str) -> None:
        """Добавляет задачу в список задач"""
        self.tasks.append(Task(title)) # добавляем задачу в список

    def show_tasks(self) -> None:
        """Выводит список всех задачь с названием и статусом"""
        for task in self.tasks: # в цикле перебираем все его элементы
            if task.is_done: # если is_done == True
                print(f'Задача "{task.title}" выполнена') # печатаем что задача выполнена
            else:
                print(f'Задача "{task.title}" не выполнена') # иначе что не выполнена

if __name__ == "__main__":
    manager = TaskManager() # создаем экземпляр класса TaskManager
    manager.add_task("Выучить Пайтон") # добавляем задачу в список
    manager.add_task("Сделать проект") # еще одеу задачу добавили
    manager.tasks[0].complete() # пометили первую задачу как выполненную
    manager.show_tasks() # выводим список задач и их статусов
