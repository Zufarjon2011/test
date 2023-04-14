##test hw1 lesson 4
number = int(input("Введите целое число: "))

if number > 0:
    number += 20
else:
    number -= 5

print("Результат:", number)


##test hw2 lesson 4

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

sum = number1 + number2

if sum % 5 == 0:
    sum += 1
else:
    sum -= 2

print("Результат:", sum)

##test hw3 lesson 4


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

nums = number1 * number2

if nums < 0:
    nums *= 8
else:
    nums *= 1.5

print("Результат:", nums)

##test hw4 lesson 4

temperature = input('enter your temperature of your body NOW: ')
temperature = float(temperature)

if temperature > 36.6:
    print('You are now sick! ')
elif temperature == temperature < 36.6:
    print('GOOD')
else:
    print('good, your temperature is good and normal! ')












