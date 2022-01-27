# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s -%(levelname)s -%(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug('this is a debug message')
# logging.info('this is a info message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')

# import json
# ar= dict(name='AR',num=10,job='programming',sts=True) #dicitionary ar is created
# arJSON = json.dumps(ar,indent=4,sort_keys=True) #indentation set to 4, and sort_keys as true which means it'llbe arranged alphabetically
# print(arJSON) #it will give you data in json format, check bool notatation for assurity

# with open('ar.json','w') as f: #written a file which contains json data for dict ar 
#     json.dump(ar,f,indent=4) #gave indentation as 4 for attractive visual appearance
# ar=json.loads(arJSON) #it will give you json data again in dict format, check bool notation for assurance
# print(ar)
# 
# import copy #copy module is imported
# a = [[1,2,3,4,5,6],[12,19,4,63,10]] # to access this list proper index is must, i.e [0][1] means first list 2nd element
# b = copy.deepcopy(a) #deep copy is independent of original list a as we can see that there is no change in list a
# b[1][2] = -10 #the value at index value 2 in 2nd list will be changed in copied list b
# print(a) #there will be no change in list a as deep shallow is indeoendent of chnage
# print(b) #only list b value will change

# import copy #copy module is imported
# a = [[1,2,3,4,5,6],[12,19,4,63,10]] #nested list is imported
# b = copy.copy(a) #shallow copy is used which means it will shallow origanlity and changes both original and copied list
# b[0][1] = -10 #the value which is at index 1 in first list is changed
# print(a) #printed original list to taste the change
# print(b) #printed copied lsit

# b = [i*2 for i in range(6)] #list b is created such that for i in list a it should multiply i to 2
# print(b) #it will give value of a as multiplied to 2

# for i in range(4):
#     for j in range(i+1):
#         print("# ", end = " ")
#     print()

# reverse triangle ::
# print("\n")
# for i in range(4):
#     for j in range(4-i):
#         print("# ", end = " ")
#     print()

# printing as RAT by taking input from user ::
# rows = int(input('num of rows:')) #user themselves will eneter the no. of rows
# for i in range(1,rows+1): #for loop is used which ranges from 1 to given no.of rows by user + 1 bcoz last no.is exclusive
#     for j in range(1,i+1): #again for loop is used such that it ranges from 1 to i + 1
#         print('a',end=' ') #for these loops, we'll print a ending with empty space
#     print() #it will print rows to next line

# reverse order ::
# rows = int(input('num of rows:')) #user themselves will eneter the no. of rows
# for i in range(rows,0,-1): #for loop is used
#     for j in range(1, i+1): #again for loop is used such that it ranges from 1 to i + 1
#         print('a',end=' ') #for these loops, we'll print a ending with empty space
#     print() #it will print rows to next line

# x = int(input()) #checks if a enetered year is aloop year or not
# if x%4 == 0 or x%400 == 0:
#     print("leap year", x)
# else:
#     print("no leap year",x)


# a = [2,3,4] #list a
# b,c,d = a  #b,c,d referred as 1st,2nd and 3rd elements in list
# # b,c,d = d,c,b print(b,c,d) this or,
# print(b,c,d) #original list will be printed
# print(d,c,b) #reversed list is printed

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# d = zip(a,b,c) #it will  zip them altogether for ex; 1,4,7 & 2,5,8 & 3,6,9 ,>
# print(set(d)) #,< as a set(you can remake it to any data type not only set however they will be zipped as tuple but under set)
# print(type(d)) # this is casted as a list

# a = ['A','R','1','0']
# b = "$".join(a) #it will join without space, for space in between do it as " ".join(a) and it comes like a r 1 0
# print(b) # a$r$1$0 will beprinted as we haven't given any empty space(" ") above
# print(7<10>9==9!='9') # checking operators precedence
# import this #just run this and it will give you random lines of statements

# import imdb
# ia = imdb.IMDb()
# search = ia.get_top250_movies()
# for movies in search:
#     print(movies)

# from tkinter import * #for all months of a specific year
# import calendar
# root = Tk()
# root.title("Gui Calendar")
# year = 2021
# myCal = calendar.calendar(year)
# cal_year = Label(root, text=myCal, font="Consolas 10 bold")
# cal_year.pack()
# root.mainloop()

# import calendar #### for specific month of a specific year
# year = int(input("year: "))
# month = int(input("month: "))
# print(calendar.month(year, month))

# from matplotlib import pyplot as plt
# x_axis = ["Dell","Laptop","Google Home","Playstation","C64","GoPro","Samsung"]
# y_axis = [21,45,35,65,50,55,70,75]
# plt.plot(x_axis,y_axis)
# plt.title("Tech Review")
# plt.xlabel("Tech Type")
# plt.ylabel("User Rat")
# plt.show()

# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Notification", "This is a notification to pc from python", threaded=True,
# icon_path=None, duration=3)
# import time
# while toaster.notification_active():
#     time.sleep(10)