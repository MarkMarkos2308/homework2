# read() and readline()
file = open(r'C:\Users\aniam\Desktop\file.txt')
f = file.read()
print(file.readlines())
print(file.readline())

s = file.read()
ind = s.find('Ani')
print(ind)

# looping thorugh a file
file = open(r'C:\Users\aniam\Desktop\file.txt')

for x in file:
    print(x)

file.close()

# with open()
with open(r'C:\Users\aniam\Desktop\file.txt', "r") as file:
    file.read(5)

# append
file = open(r'C:\Users\aniam\Desktop\file.txt', "a")
file.write("this is a new text")
file.close()

# write
file2 = open(r'A ' "w")
file2.write("i deleted everything and this is my new text")
file2.close()

# list of lines
list_of_lines = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

file2.write("Hello \n")
file2.writelines(list_of_lines)
file2.close()

# creating
file3 = open(r'C:\Users\aniam\Desktop\file25.txt', "x")
file3.write("Hello \n")
file3.close()

# problem 2
for i in range(1, 4):
    f = open(fr'C:\Users\aniam\Desktop\file{i}.txt', "x")
    f.write(f"write text {i}")

# remove
import os
os.remove(r'C:\Users\aniam\Desktop\file2.txt')
