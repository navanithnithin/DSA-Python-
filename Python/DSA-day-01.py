print("HI this is nithin S")
list1=[2200,2350,2600,2130,2190]
list1[4]=list1[4]-190
print(list1)
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panter')
print(heros)
heros.pop()
print(heros)
heros.insert(3,"black panter")
print(heros)
heros[1:3]=['doctor strange']
print(heros)
# num=int(input("enter the num "))
# list2=[]
# for x in range(1,num,2):
#     list2.append(x)
# print(list2)

class Parrot: 
 
    # class attribute 
    species = "bird" 
 
    # instance attribute 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
 
# instantiate the Parrot class 
blu = Parrot("Blu", 10) 
woo = Parrot("Woo", 15)

print("what is the species {}".format(woo.__class__.species))


