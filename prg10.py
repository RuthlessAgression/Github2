# w, x, y, z = input("any 4 nums:").split()
# print(w, x, y, z) #all 4 values in same line
# # print(x)
# # print(y)
# # print(z) #it will print those 4 nums seperately

# a = 20
# b = 30
# c = 4
# conds = [ # it is used when conditions are more than 2 by making list of conditions
#     a<19,
#     b>=32,
#     c!=4,
# ]
# if all(conds): #if you want to check if any od the list conds are proper you can use any instead of all as or instead of and
#     print("alright") #as the all conditions are not correct, it will move to else block
# else: #if if block fails it will print statement from else block
#     print("back off")

# a = 20
# b = 30
# print(a,b)
# temp = a # a is declared to temp
# a = b # so here a was empty then b declared to a
# b = temp # now b was empty then temp is declared to b

# a = a + b # new value of a is 20 + 30 = 50
# b = a - b # new value of b is 50 - 30 = 20
# a = a - b # new value of a is 50 - 20 = 30(

# a,b = b,a #coolest method to swap vars in python
# print(a,b)

# a = [1,2,3,1,4,2,5,6,2,2,1,1,2,9]
# print(a) # it will print list a as it is
# print(set(a)) #it will print list as a set for unique value
# b = max(set(a), key= a.count) #it will look to set a for maximum repeated no. by a.count method
# print(b) #it will print that maximum repeated no.

# a = [] #empty list a is created
# b = [] #empty list a is created
# for i in range(11): #for loop is used to use nums betn range 11
#     if i % 2 != 0: #if i divided by 2 doesn't equal to 0 which are odd nums betn range of 11
#         a.append(i**2) #if this condition matches list a will append those odd nums as squared(i**2)
#     elif i % 2 == 0:
#         b.append(i**2) #if this condition matches list a will append those even nums as squared(i**2)
#     else: #if both condition should fail this block will be executed
#         print("back off")
# print(a) #it will print those squared odd nums
# print(b) #it will print those squared even nums

# a = [i**2 for i in range(11) if i%2 != 0] #short method to print squared odd nums
# print(a) #you can do same for squared even nums by making i%2 == 0

# def sum(*a): #(*a) will allow numerous no. of parameters in sum function
#     result = 0 # result var is initialzed as o
#     for i in a: #for loop is used to acces given parameters of func sum
#         result += i #as a new result, it will add to i
#     return result # then it will return result
# res = sum(2,3,4,1) #var res is used to hold the attributes of func sum
# print(res) # it will print the summed value which should be 10(2+3=5+4=9+1=10)

# a = "rar"
# b = a.find(a[::-1]) == 0
# print(b)
# c = 'is palindrome'
# print(f'b,{c}')
# # b = a[::-1]
# # if a == b:
# #     print("palindrome")

# for i in range(5):
#     for j in range(0, i):
#     	print("*",end=" ")
#     print()
# for i in range(4):
#     for j in range(i+1):
#     	print("* ",end="")
#     print()

# import pywhatkit
# pywhatkit.text_to_handwriting(""" python
# is a programming
# language""", save_to="mytext", rgb=(0,0,225))

# from tkinter import *
# filename = "words.txt"
# data = open(filename,"r")
# window  = Tk()
# biglist = []
# for line in data:
#     biglist.append(line.strip().lower())
# v = StringVar()
# v1 = StringVar()
# def check():
#     thingy = str(v.get().lower())
#     if thingy in biglist:
#         v1.set("It is Correct.")
#     else:
#         v1.set("It is incorrect.")
# l = Label(window,text="Scrabble Word Checker",font=("Ubuntu",60)).grid(row=0,column=3)
# l1 = Label(window,text="Please Enter a word:",font=("Ubuntu",20)).grid(row=1,column=3)
# l2 = Label(window,text="Is it Correct?",font=("Ubuntu",20)).grid(row=3,column=3)
# b = Button(window,text = "Check Spelling",command=check,font=("Ubuntu",20)).grid(row =6,column=3)
# e = Entry(window,textvariable=v,font=("Ubuntu",20)).grid(row=2,column=3)
# e1 = Entry(window,textvariable=v1,font=("Ubuntu",20)).grid(row=4,column=3)
# window.mainloop()