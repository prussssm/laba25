import threading
import time

# Глобальные переменные
global_matrix = None
matrix_changed = False
matrix_lock = threading.Lock()

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def task_1(array1, array2):
    return [array1, array2]

def task_2(array1, array2, array3):
    return [array1, array2, array3]

def input_array():
    return list(map(int, input("Введите элементы массива через пробел: ").split()))

def main_menu():
    print("\nГлавное меню:")
    print("1. Задача 1")
    print("2. Задача 2")
    print("3. Выход")

def rotation_task():
    global global_matrix, matrix_changed
    while True:
        if matrix_changed:
            with matrix_lock:
                if matrix_changed:
                    global_matrix = rotate_matrix(global_matrix)
                    print("Матрица повернута:")
                    for row in global_matrix:
                        print(row)
                    matrix_changed = False
        time.sleep(0.1)  # Небольшая задержка, чтобы не нагружать ноут

def main():
    global global_matrix, matrix_changed
    
    # Запуск потока для поворота матрицы
    rotation_thread = threading.Thread(target=rotation_task, daemon=True)
    rotation_thread.start()
    
    while True:
        main_menu()
        choice = int(input("Выберите пункт меню: "))
        
        if choice == 1:
            array1 = input_array()
            array2 = input_array()
            with matrix_lock:
                global_matrix = task_1(array1, array2)
                matrix_changed = True
            print(f"Результат задачи 1: {global_matrix}")
        elif choice == 2:
            array1 = input_array()
            array2 = input_array()
            array3 = input_array()
            with matrix_lock:
                global_matrix = task_2(array1, array2, array3)
                matrix_changed = True
            print(f"Результат задачи 2: {global_matrix}")
        elif choice == 3:
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()