# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

print("Введите вещественное число")
number = input()
sum = 0
str = number.split(".")
number = int (str[0])
number1 = int (str[1])
while number > 1 :
    sum += int (number % 10)
    number/=10
while number1 > 1 :
    sum += int (number1 % 10)
    number1/=10
print (sum)