def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    povitIndex = start
    povit = elements[povitIndex]
    while start < end:
        while start < len(elements) and elements[start] <= povit:
            start += 1
        while elements[end] > povit:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(povitIndex, end, elements)
    return end


def QuickSort(elements, start, end):
    if start < end:
        p = partition(elements, start, end)
        QuickSort(elements, start, p - 1)
        QuickSort(elements, p + 1, end)


if __name__ == "__main__":
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
    ]
    for i in tests:
        QuickSort(i, 0, len(i) - 1)
        print(i)
