def meargSort(array, key, descending=False):
    if len(array) <= 1:
        return
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    meargSort(left, key, descending)
    meargSort(right, key, descending)
    meargTwoSortedArray(left, right, array, key, descending)


def meargTwoSortedArray(a, b, array, key, descending):
    i = j = k = 0
    # merged = []
    if descending:
        while i < len(a) and j < len(b):
            if a[i][key] >= b[j][key]:
                array[k] = a[i]
                i += 1
            else:
                array[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            array[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            array[k] = b[j]
            j += 1
            k += 1
    else:
        while i < len(a) and j < len(b):
            if a[i][key] <= b[j][key]:
                array[k] = a[i]
                i += 1
            else:
                array[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            array[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            array[k] = b[j]
            j += 1
            k += 1

    # another implementation
    # if descending:
    #     while len(a) > 0 and len(b) > 0:
    #         if a[0][key] <= b[o][key]:
    #             merged.append(a.pop(0))
    #         else:
    #             merged.append(a.pop(0))

    # else:
    #     while len(a) > 0 and len(b) > 0:
    #         if a[0][key] >= b[0][key]:
    #             merged.append(a.pop(0))
    #         else:
    #             merged.append(a.pop(0))

    return array
    # return merged


if __name__ == "__main__":
    # elements = [9, 1, 5, 66, 45, 36, 92, 234, 47, 111, 4]
    elements = [
        {"name": "vedanth", "age": 17, "time_hours": 1},
        {"name": "rajab", "age": 12, "time_hours": 3},
        {"name": "vignesh", "age": 21, "time_hours": 2.5},
        {"name": "chinmay", "age": 24, "time_hours": 1.5},
    ]
    print(elements)
    meargSort(elements, "age",True)
    print(elements)
