# def addToNumbers(x=10,y=35):
#     return x+y

# print(addToNumbers(10,40))
# print(addToNumbers(90))
# print(addToNumbers())

# def details(name,age):
#     print("name :{}".format(name))
#     print("age : ",age)
# print(details(age=60, name="raghu"))
# print(dir(details))

from collections import Counter
x=[4,22,46,78,9,93,100,93,100,4,4,46]
y=Counter(x)
print(y)


def dec(num):
    x = num >> 1 + (4 & 1)
    print(x)

name={}
print(type(name),dir(name))
dec(4)
