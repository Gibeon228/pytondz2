# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print ("Введите целочисленно число N>=1")
N = int(input())
if (N>2) :
    list1=["1", "1"]
    list2 = [1, 1]
    for i in range (2, N):
        list1.append(list1[i-1] +"*" + str (i))
        list2.append(list2[i-1] * i)
    list1.remove("1")
    list2.remove(1)
    print(list1)
    print(list2)
elif (N==1):
    print(1)
