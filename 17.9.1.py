def binary_search(arr, x):
    """
    Функция для реализации алгоритма двоичного поиска.
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


def sort_list(arr):
    """
    Функция для сортировки списка по возрастанию элементов.
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# ввод последовательности чисел
while True:
    try:
        num_list = input("Введите последовательность чисел через пробел: ").split()
        num_list = [int(num) for num in num_list]
        break
    except ValueError:
        print("Ошибка: в последовательности должны быть только числа.")

# ввод числа, которое нужно найти
while True:
    try:
        x = int(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")

# сортировка списка
num_list = sort_list(num_list)

# поиск позиции элемента
pos = binary_search(num_list, x)
if pos == -1:
    print("Число", x, "не найдено в последовательности.")
else:
    if pos == 0:
        print("Число", x, "меньше всех элементов в последовательности.")
    elif pos == len(num_list) - 1:
        print("Число", x, "больше всех элементов в последовательности.")
    else:
        print("Число", x, "находится между элементами с индексами", pos - 1, "и", pos)