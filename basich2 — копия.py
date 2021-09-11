# homework
print('Homework')
print(":                        ///                       ")

# problem 1
number = int(input("Enter number"))
m = number % 2
if m == 0:
    print('odd')
else:
    print('even')

print(":                        ///                       ")

# problem 2
number2 = int(input('number'))
uuu = number2 % 3
if uuu == 0:
    print('divisible by 3')
else:
    print('not divisible by 3')

print('                         ///')

# problem 3
# > 95                             A
#  85 - 95                         B
#  65 - 84                         C
# < 65                             D
grade = int(input('grade'))
if grade >= 95:
    print('A')
elif 95 > grade >= 85:
    print('B')
elif 85 > grade >= 66:
    print('C')
elif grade < 65:
    print('D')

print('                         ///')

# problem 4
number1_7 = int(input('print number "1-7"'))
if number1_7 == 1:
    print('Sunday')
if number1_7 == 2:
    print('Monday')
if number1_7 == 3:
    print("Tuesday")
if number1_7 == 4:
    print('Wednesday')
if number1_7 == 5:
    print("thursday")
if number1_7 == 6:
    print('Friday')
if number1_7 == 7:
    print('Saturday')

print('                         ///')

# problem 5
age = int(input('print your age'))
grade2 = int(input('print your garde'))
if age >= 17 and grade2 >= 9:
    print("You can get a license")
if age < 17 or grade2 < 9:
    print("You don't can get a license")

print('                         ///')

# problem 6
a = int(input('number 1'))
b = int(input('number 2'))
if a < b:
    print(str(a) + ' is small')
if a > b:
    print(str(b) + ' is small')

print('                         ///')

# problem 7
number3 = float(input('enter number'))
if number3 == 0:
    print('equal to 0')
if number3 > 0:
    print('positive')
if number3 < 0:
    print('negative')

print('                         ///')

# problem 8
grade_english = int(input('enter your grade english'))
grade_math = int(input('enter your grade math'))
if grade_math >= 20 and grade_english >= 0:
    print("you can be accepted")
if grade_math >= 10 and grade_english >= 10:
    print("you can be accepted")
if grade_math >= 0 and grade_english >= 20:
    print("you can be accepted")
if grade_math >= 15 and grade_english >= 5:
    print("you can be accepted")
if grade_math >= 5 and grade_english >= 15:
    print("you can be accepted")

