# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

print ("Введите число к")
k = int(input())
list = [1]
sum = 1
for i in range(1, k):
    list.append((1+1/i) ** i)
    sum += list[i]
print (list)
print (sum)