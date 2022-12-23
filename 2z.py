#Задайте список из n чисел последовательности (1 + 1/nIIIIII)**n, выведеите его на экран, а так же сумму элементов списка.
#Пример:
#Для n=4 -> [2, 2.25, 2.37, 2.44]
#Сумма 9.06

n = int (input('Введите n '))
print (n)
list = []
sum = 0
for i in range (1, n+1):
    i = round ((1 + 1/i) ** i, 3)
    list.append (i) 
    sum = sum + i  
print (list)
print (sum)