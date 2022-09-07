# Реализуйте алгоритм перемешивания списка.
import random
list1 = [1, 4, 5, 12, 3]
list2 = []
a = 0
help = 0
for i in range(len(list1)):
    a = random.randint(0, len(list1)-1)
    help = list1[i]
    list1[i] = list1[a]
    list1[a] = help
print (list1)
