import os
# read() and readline()
# a = 'apple'
# file = open('C:\Users\User\Desktop\basiq py\homework\1file.txt', "r")
# f = file.read()
# print(file.readline())
#
# print(file.read())


# a = 5
# v = "str"
#
# try:
#     print(a + v)
# except TypeError:
#     print("you can't add a number to an integer")+

# a = []
# v = a.append('basketball')
# b = a.append('Ani')
# a.remove("basketball")
# a.remove("Anime")
# print(a)
# while a != str:
#     x = a[0]
#     a.remove(x)
#     if len(a) == 0:
#         break
#     print(a)
# a = ['Gij']
# print(a.read())
# x = a.append('Pupush pingvin')
# v = str(a)
# f = v.strip("[]")
# print(f)
# f = (r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "w")
# f.writhe('writhe')
# f.clouse()
# f = (r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "w")
# print(f.read)
#
# f.write("the new content")
# f.close()
# # open and read the file after the appending:
# f = open(r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "r")
# print(f.read())
# f = open(r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "a")
# f.write(' append')
# f.close()
# f = open(r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "r")
# print(f.read())
# file1 = open(r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "w")
# list_of_lines = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.write("Hello \n")
# file1.writelines(list_of_lines)
# file1.close()
# file1 = open(r"C:\Users\User\Desktop\basiq py\pingvinto.txt", "r")
# print(file1)
# c = 1
# while c < 4:
#     if c == 1:
#         a = open(r'C:\Users\User\Desktop\basiq py\file1.txt', 'w')
#         a.write('this is file1')
#         a.close()
#         a = open(r'C:\Users\User\Desktop\basiq py\file1.txt', 'r')
#         print(a.read())
#     if c == 2:
#         b = open(r'C:\Users\User\Desktop\basiq py\file2.txt', 'w')
#         b.write('this is file2')
#         b.close()
#         b = open(r'C:\Users\User\Desktop\basiq py\file2.txt', 'r')
#         print(b.read())
#     if c == 3:
#         f = open(r'C:\Users\User\Desktop\basiq py\file3.txt', 'w')
#         f.write('this is file3')
#         f.close()
#         f = open(r'C:\Users\User\Desktop\basiq py\file3.txt', 'r')
#         print(f.read())
#         break
#     c += 1


thisdict = {}


#
# print(thisdict)

# a = input('your name')
# b = input('your username')
# c = input('your email')
# d = input('your age')
# information = {
#     'name': a,
#     'username': b,
#     'age': d,
#     'email': c,
#
# }
# print(information.keys())


# x = ['phone number', 'country']
# y = ['+374xxxxxxxx', 'Armenia']

# for z in x:
#     a = z
# for c in y:
#     b = c
# g = {
#     z: c
# }

#
# for i in range(len(x)):
#     thisdict.update({x[i]: y[i]})
#     print(thisdict)
# z = input("name")
#
#
# def a():
#     adictioari = {
#         'year': '2021',
#         'name': z,
#         'virus': 'corona',
#         'answer': '+'
#     }
#     adictioari2 = adictioari.copy()
#     adictioari2.clear()
#     adictioari2.update({"you": z})
#     return adictioari2
#
#
#
# tp = ('winter', 'summer')
# tp = list(tp)
# list_1 = ['fall', 'spring']
# list_1 = list_1 + tp
# print(tuple(list_1))

# a = ('winter', 'summer')
# a = list(a)
# a.clear()
# print(tuple(a))

# tp = ('winter', 'summer')
# ls = list(tp)
# ls.clear()
# print(ls)
# ls = tuple(ls)

# this_set = {'apple', 'banana', 'cherry'}
# for d in this_set:
#     if d == 'banana':
#         print('true')
# this_set.add('orange')
# print(this_set)

thisset = {"apple", "banana", "cherry", 3}
# tropical = ["pineapple", "mango", "papaya"]
# thisset.update(tropical)
# thisset.discard("apple")
# print(thisset)

# set1 = {1, 2, 3}
set2 = {3, 4, 5}
# set3 = set1.union(set2)
# print(set3)
z = thisset.intersection(set2)
print(z)

