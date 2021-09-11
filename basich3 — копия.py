print('homework 3')

import math


# problem 1
def m(z=100000, name='user'):
    e = "Employee named " + name + ' earns ' + str(z)
    return e


print(m(int(input("enter your earnings |")), input('enter your name |')))

print(' //////////////////////////////////////////////////////////////////////////////////////////////////////////////')


# problem 2
def s(number1, number2, number3):
    if number2 > number1 > number3 or number2 < number1 < number3:
        print('he is in the middle')
    else:
        print('it is not in the middle')


print(s(int(input('enter number 1 |')), int(input('enter number 2 |')), int(input("enter number 3 |"))))

print(' //////////////////////////////////////////////////////////////////////////////////////////////////////////////')


# problem 3
def o(n1, n2, n3):
    if n1 < n2 > n3:
        print('n2 more')
    if n2 < n1 > n3:
        print('n1 more')
    if n2 < n3 > n1:
        print('n3 more')


o(int(input('print number 1 |')), int(input('print number 2 |')), int(input('print number 3 |')))

print(' //////////////////////////////////////////////////////////////////////////////////////////////////////////////')


# problem 4
def c(h, r):
    p = math.pi * h * r ** 2
    return p


print(c(int(input('print h |')), int(input('print r |'))))

print(' //////////////////////////////////////////////////////////////////////////////////////////////////////////////')


# problem 5
def calculator(number1, a, number2):
    if a == '+':
        print(number1 + number2)
    if a == "-":
        print(number1 - number2)
    if a == "/":
        print(number1 / number2)
    if a == '*':
        print(number1 * number2)
    if a == "**":
        print(number1 ** number2)
    if a == '/' and number1 == 0 or number2 == 0:
        print("operation can not be completed.")


print(calculator(int(input('Enter number 1')), input('Enter action'), int(input('Enter number 2'))))

print(' //////////////////////////////////////////////////////////////////////////////////////////////////////////////')

# problem 6
a = input('print something')
b = int(a)
