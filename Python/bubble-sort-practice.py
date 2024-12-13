def bubbleSort(elements, type):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if elements[j][type] > elements[j + 1][type]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
        if swapped == False:
            break
    return elements


if __name__ == "__main__":
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
    ]
    print(elements)
    print(bubbleSort(elements, "name"))
