def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if array[middle] != array[-1] and array[middle] < element <= array[middle + 1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif array[middle] != array[-1]:
        return binary_search(array, element, middle + 1, right)
    else:
        return False


if __name__ == '__main__':
    array = None
    element = None
    while array is None or element is None:
        if array is None:
            try:
                array = list(map(int, input("Введите последовательность чисел через пробел\n").split()))
            except ValueError:
                print("Вы ввели не корректную последовательность чисел\n")
                continue
        if element is None:
            try:
                element = int(input("Введите число\n"))
            except ValueError:
                print("Необходимо ввести целое число\n")
                continue

    array = merge_sort(array)
    print(f"Массив чисел после сортировки: {array}\n")
    result = binary_search(array, element, 0, len(array) - 1)

    if result:
        print(f"{result} - номер позиции элемента, который меньше числа {element}, а следующий за ним больше или равен этому числу\n")
    else:
        print(f"Элемента, который меньше числа {element}, а следующий за ним больше или равен этому числу, нет\n")
