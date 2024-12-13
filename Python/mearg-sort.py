def meargSort(array):
    if len(array) <= 1:
        return
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    meargSort(left)
    meargSort(right)
    meargTwoSortedArray(left, right, array)


def meargTwoSortedArray(element1, element2, array):
    i = j = k = 0
    # arr = []
    while i < len(element1) and j < len(element2):
        if element1[i] > element2[j]:
            array[k] = element2[j]
            # arr.append(element2[j])
            j += 1

        else:
            array[k] = element1[i]
            # arr.append(element1[i])
            i += 1
        k += 1
    while i < len(element1):
        array[k] = element1[i]
        # arr.append(element1[i])
        i += 1
        k += 1
    while j < len(element2):
        array[k] = element2[j]
        # arr.append(element2[j])
        j += 1
        k += 1

    return array


if __name__ == "__main__":
    element1 = [5, 98, 57, 43, 81, 8, 12, 56, 78, 99, 105]
    element2 = [7, 9, 45, 51, 56]
    # print(meargTwoSortedArray(element1, element2))
    meargSort(element1)
    print(element1)
