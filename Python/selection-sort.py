def selectionSort(element):
    size = len(element)
    for i in range(size):
        minIndex = i
        for j in range(minIndex + 1, size):
            if element[j] < element[minIndex]:
                minIndex = j
        if i != minIndex:
            element[i], element[minIndex] = element[minIndex], element[i]


if __name__ == "__main__":
    elements = [78, 12, 15, 8, 61, 53, 23, 27]
    selectionSort(elements)
    print(elements)
    # print(findMinimumElement(elements))
