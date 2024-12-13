def swap(start, end, elements):
    elements[start], elements[end] = elements[end], elements[start]


def partition(elements, start, end):
    pivotIndex = start
    pivot = elements[end]
    # while start < end:
    #     while start < len(elements) and elements[start] <= pivot:
    #         start += 1
    #     while elements[end] > pivot:
    #         end -= 1
    #     if start < end:
    #         swap(start, end, elements)

    for i in range(start, end):
        if elements[start] <= pivot:
            swap(i, pivotIndex, elements)
            pivotIndex += 1
    swap(pivotIndex, end, elements)
    return end


def QuickSort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        p = partition(elements, start, end)
        QuickSort(elements, start, p - 1)
        QuickSort(elements, p + 1, end)


if __name__ == "__main__":
    tests = [
        [11, 9, 29, 7, 2, 15, 28,8],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
    ]

    for i in tests:
        QuickSort(i, 0, len(i) - 1)
        print(i)
