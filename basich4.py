print('homework')

# problem 1

a = input("enter your username")
b = input('enter your name')

print(a[:4] + b + a[4:])

# problem 2


s1 = "qwerty"
s2 = "asdfg"
s3 = "tyu"
s4 = "1234"
s5 = "p"

d = s1[0] + s2[0] + s3[0] + s4[0] + s5[0]
c = s1[5] + s2[4] + s3[2] + s4[3] + s5[0]

print(d)
print(c)
# problem 3

name1 = input('name')
namelen = int(len(name1))

if namelen % 2 == 1:
    print(name1.upper())
if namelen % 2 == 0:
    print(name1)

# problem 4

CNN = """The University of Virginia has disenrolled 238 students for its fall semester on Friday for not 
complying with the university's Covid-19 vaccine mandate, according to a university spokesperson.
UVA requires "all students who live, learn, or work in person at the university" to be fully vaccinated 
for the upcoming 2021-2022 academic year, according to current university Covid-19 policies.
Out of the 238 incoming Fall semester students, only 49 of them were actually enrolled in classes, and the remaining 
189 "may not have been planning to return to the university this fall at all," UVA spokesperson Brian Coy told CNN.
"Disenrolled means you're not eligible to take courses," Coy said. 
He added that students who were enrolled at the university on Wednesday still have a week to update their status 
at which point they can re-enroll."""

print(CNN.count("university"))
print(CNN.count("vaccine"))
print(CNN.count("student"))
print(CNN.count("1"))
print(CNN.count("2"))
print(CNN.count("3"))
print(CNN.count("4"))
print(CNN.count("5"))

# problem 5

if "2021-2022" in CNN:
    print(CNN.replace("2021-2022", ""))

# problem 6

h = input('string')
k = h[:5]
m = h[6:]
print(k.upper() + m)

# problem 7

v = input('Enter your name')
f = input("Enter your (furute) profession")
print(f'I am {v} and I am a {f}.')


# problem 8

MW = (input('3 digit number'))
if 100 <= int(MW) <= 999:
    print(MW[2] + MW[1] + MW[0])
else:
    print('Eror')
