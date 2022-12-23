#Реализуйте алгоритм перемешивания списка. 
#НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
n = int (input('Введите длину списка '))
my_list = list (range (n))
print (my_list)

from random import randrange
new_list = my_list
for i in range (n):
   j = randrange (n)
   t = new_list[i]
   new_list [i] = new_list[j]
   new_list[j] = t
print (new_list)