from random import randint
lst = [randint(0, 9) for i in range(15)]
print(lst)
your_number = int(input("Please, enter your number in range from 1 to 9: "))
print("Your number`s index is " + str(lst.index(your_number)) + ".")