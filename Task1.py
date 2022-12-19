# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def list_of_prime_factors(): 
    num = int(input("Введите число: "))
    i = 2 
    lst = []
    old = num
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} : {lst}")

list_of_prime_factors()