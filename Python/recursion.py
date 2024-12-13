# def sum(val):
#     if val == 1:
#         return 1
#     return val + sum(val - 1)


# print(sum(10))

# fin


# def fib(num):
#     if num == 0 or num == 1:
#         # print(num)
#         return num
#     # print(fib(num - 1), fib(num-2))
#     return fib(num - 1) + fib(num-2)


# if __name__ == "__main__":
#     print(fib(10))


# def sumOfList(arr):
#     if len(arr) == 1:
#         return arr[0]

#     return arr[0] + sumOfList(arr[1:])


# print(sumOfList([5, 6, 7, 8, 10, 9]))


# def toString(n, base):
#     constStr = "0123456789ABCDFE"
#     if n < base:
#         return constStr[n]
#     else:
#         return toString(n // base, base) + constStr[n % base]


# print(toString(2835, 16))


# def listRecursion(arr):
#     total = 0
#     for i in arr:
#         if type(i) == type([]):
#             total =total+ listRecursion(i)
#         else:
#             total = total+ i
#     return total


# print(listRecursion([8, 9, [3, 5]]))


# def fact(num):
#     if num == 0:
#         return 1
#     if num >= 1:
#         return num * fact(num - 1)
#     return "Negative number"

# print(fact(5))


# def fib(num):
#     if num <= 1:
#         print(num)
#         return num
#     if num > 1:
#         return fib(num - 1) + fib(num - 2)


# print(fib(10))


def sumOf(num):
    if num == 0:
        return num
    else:
        return num%10 +sumOf(num//10)
    
print(sumOf(75))
