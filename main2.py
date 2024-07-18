# 2 - делится на 1 и на 2
# 3 - делится на 1 и на 3
# 5 - делится на 1 и на 5

# непростое число: 4 - делится на 1, на 2 и на 4
# непростое число: 6 - делится на 1, на 2, на 3 и на 6

# сравнение числа с 1, меньше или равно оно 1, если да, то тогда мы возвращаем false
# создаем цикл, который перебирает все числа от 2 до квадратного корня числа включительно
# проверяем делится ли наше число на какое-то из чисел, которые перебирает цикл без остатка

import math

def is_prime(number):
   if number <= 1:
       return False

   for i in range(2, int(math.sqrt(number)) + 1):
       if number % i == 0:
           return False

   return True

print(is_prime(6))

