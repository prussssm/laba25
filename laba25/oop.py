import time
from memory_profiler import memory_usage
from abc import ABC, abstractmethod

# Абстрактный класс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретные команды
class Task1Command(Command):
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def execute(self):
        return list(map(lambda x, y: x + y, self.array1, self.array2))

class Task2Command(Command):
    def __init__(self, array1, array2, array3):
        self.array1 = array1
        self.array2 = array2
        self.array3 = array3

    def execute(self):
        return list(map(lambda x, y, z: x + y + z, self.array1, self.array2, self.array3))

class RotateMatrixCommand(Command):
    def __init__(self, matrix):
        self.matrix = matrix

    def execute(self):
        return [list(reversed(col)) for col in zip(*self.matrix)]

class MatrixManipulator:
    def input_array(self, prompt="Введите элементы массива через пробел: "):
        return list(map(int, input(prompt).strip().split()))

    def get_matrix_input(self, rows_count):
        return [self.input_array(f"Введите ряд {i + 1} матрицы через пробел: ") for i in range(rows_count)]

# Инвокер (вызывающий)
class CommandInvoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            start_time = time.time()
            mem_usage = memory_usage(self.command.execute)
            end_time = time.time()

            result = self.command.execute()
            print("Результат:", result)
            print(f"Время выполнения: {end_time - start_time:.6f} секунд")
            print(f"Максимальное использование памяти: {max(mem_usage)} MiB")
        else:
            print("Команда не установлена")

class Menu:
    def __init__(self):
        self.manipulator = MatrixManipulator()
        self.invoker = CommandInvoker()

    def display(self):
        print("\nГлавное меню:")
        print("1. Задача 1")
        print("2. Задача 2")
        print("3. Повернуть матрицу")
        print("4. Выход")

    def run(self):
        while True:
            self.display()
            choice = input("Выберите пункт меню: ")

            if choice == '1':
                array1 = self.manipulator.input_array()
                array2 = self.manipulator.input_array()
                command = Task1Command(array1, array2)
                self.invoker.set_command(command)
                self.invoker.execute_command()

            elif choice == '2':
                array1 = self.manipulator.input_array()
                array2 = self.manipulator.input_array()
                array3 = self.manipulator.input_array()
                command = Task2Command(array1, array2, array3)
                self.invoker.set_command(command)
                self.invoker.execute_command()

            elif choice == '3':
                rows_count = int(input("Введите количество рядов матрицы: "))
                matrix = self.manipulator.get_matrix_input(rows_count)
                command = RotateMatrixCommand(matrix)
                self.invoker.set_command(command)
                self.invoker.execute_command()

            elif choice == '4':
                print("Завершение работы программы.")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu = Menu()
    menu.run()