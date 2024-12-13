def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                a = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = a
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [2, 67, 48, 3, 4, 56, 12, 92, 10, 27, 122, 23, 46, 58, 84]
    print(elements)
    bubble_sort(elements)
    print(elements)
