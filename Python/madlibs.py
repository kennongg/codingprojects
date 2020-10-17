import random

f = open('madlibs.txt', 'r')

madlibsText = f.readlines()

madlibs = random.choice(madlibsText)

noun = input("Enter a noun : ")
noun2 = input("Enter another noun : ")

madlibs = madlibs.replace("blank2", noun2).replace("blank", noun)


print(madlibs)
