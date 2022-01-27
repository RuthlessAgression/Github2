# a = [1,2,3,4,5,6] #list a is created
# b = [i*i for i in a] #var b includes a list which contains square value of previous list
# print(a) #it will get you origial list
# print(b) #it will get you new list with new value

# a = [1,2,3,4,5,6]
# b = tuple(a)
# print(b)
# i1, *i2, i3 = b #so basically, we declared i1 & i3 as first & last, while everything comes between them is upto i3
# print(i1) #it will give you first no.
# print(i2) #it will give you all no. between i1 and i3
# print(i3) #it will give you last no.

# import sys #sys module is imported
# a = [1,2,'ar',5,'ra',6] # list a is induced
# b = [7,8,9,'hello',10] #list b is induced with different value than list a
# print(sys.getsizeof(a),'bytes')
# print(sys.getsizeof(b),'bytes')

# shrtct tips :: shift+alt+down/up = copy line down/up
#               alt+down/up = move line down/up

# import timeit #timeit mpdule is imported
# print(timeit.timeit(stmt='[1,2,3,4,5,6]',number=1000)) #timespan of execution is printed
# print(timeit.timeit(stmt='[1,2,3,4,5,6]',number=1000)) #same shit is applied for diff. code line

# a = dict(ram = 'name',ten = 'num',AR = 'WM') #made dictionary using dict function
# print(a) #printed a as a dictionary
# try: #used try block to test the code
#     print(a['ra']) #tested if there is any key like 'ra' if yes it will return its value
# except: #used except block to prevent error
#     print('not found') #if try block should fail, it will print this statement

# b = {9,9,3,3,8,7,66,68,73}
# a = {2,3,3,42,5,1,98}
# c = {12,19,4,63,10}

# print(a.union(b)) #it will give all the values in set a and set b
# print(a.intersection(b)) ##it will give intersection value which is only 3 in between set a and set b
# print(a.issubset(b)) # it will give you false
# print(a.isdisjoint(c)) # it will give you true coz set a and set c have no common value

# a = frozenset({2,3,3,42,5,1,98}) #you should try frozenset when you want unique value alongside no further changes.
# try:
#     print(a.remove(1)) #it will give you an error coz frozenser is immutable as tuple
# except:
#     print('frozen set is immutable')

# a = 'hello ar10'
# print(a[:]) #it will print whole string
# print(a[:5]) #it will print just hello
# print(a[::2]) #it will print str with dfference of index value 2
# print(a[::-1]) #it will print whole str in reverse order i.e starting from -1 to o
# print(a[1:]) #it will print whole str excluding e which has index value of 0

# a = 'hello,are,you,ar10'
# print(a.split(',')) #it will split every word into particular str which is differentiated by ','
# a = 18.456324 #a as a float value
# print('a is %.2f'%a) #it will give only two no.after .

# from itertools import * #from itertools every data is imported as we used * instead of naming certain module
# # a = [1,2,3] # list a is created
# # for i in repeat(1, 5): #used for loop such that it should repeat 1 for 5times
# #     print(i) #printed i to get five 1
# for i in count(7): #it will start to count from 7 to infinity unless certain if condition are given
#     print(i)
#     if i == 15: #when i equals to 15,>
#         break # ,<it will stop counting and breaks after reaching 15

# a = [1,2,3] #list a is created
# b = [i*2 for i in a] #list b is created such that for i in list a it should multiply i to 2
# print(b) #it will give value of a as multiplied to 2

# try: #try block is induced
#     a = 5/0
#     # c = a + '10'
# except Exception as b: #declared exception to var b
#     print(b) #will give the exception occured
# # except TypeError as d: #declared exception to var d
#     print(d) #will give the exception occured

# a = [2,3,4]
# b = (3,6,9)
# print(tuple(map(str,a))) #it will map elememts of a list(a) as a str under tuple
# print(list(map(str,b))) #it will map elememts of a tuple(b) as a str under list

# a = [2,3,4]
# for i,j in enumerate(a): #i for index and j for elements in the list
#     print(i,j) #it will print elements in list along with their index

# from captcha.image import ImageCaptcha
# image = ImageCaptcha(width=280,height=90)
# captcha_text = 'AR10'
# data = image.generate(captcha_text)
# image.write(captcha_text, "CAPTCHA.png")