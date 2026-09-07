import random
def f1():
    return 1
def f3():
    return 2
def f4():
    return 3
def f5():
    return 4
numberList = [f1,f3,f4,f5]
print("random item from list is: ", random.choice(numberList)())