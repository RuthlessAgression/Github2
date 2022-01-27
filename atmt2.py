# simple login widget
# from tkinter import *
# from tkinter import messagebox

# def Ok():
#     uname = e1.get()
#     password = e2.get()
    
#     if(uname == " "and password == " "):
#         messagebox.showinfo(" ", "Blank not allowed")
#     elif(uname == "Arten" and password == "@lmar10#"):
#         messagebox.showinfo(" ","Login Successfull")
#         root.destroy()
#     else:
#         messagebox.showinfo(" ","Incorrect uname & pw")

# root = Tk()
# root.title("Login")
# root.geometry("300x200")

# global e1
# global e2

# Label(root, text="UserName").place(x=10, y=10)
# Label(root, text="Password").place(x=10, y=40)

# e1 = Entry(root)
# e1.place(x=140, y=10)
# e2 = Entry(root)
# e2.place(x=140, y=40)
# e2.config(show="*")

# Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=100)
# root.mainloop()

# import subprocess #module name sub process is imported
# ## path = r'path/to/your/file.txt' #created file path
# subprocess.Popen(["notepad.exe"]) #it will open notepad

# import string # string module is imported
# from random import * # from random module everyting is imported
# value = string.ascii_letters + string.punctuation + string.digits # value var contains str letters,punctuation&digits
# password = "".join(choice(value) for i in range(randint(8, 16))) #pw var is created that joins&chooses from value from 8-16 chars
# print("\n Auto Generated Password:", password) # it will print the auto generated password in new line

# import os # os module is imported firstly
# check = input("need to turn off ? (Yes/No): ") asks user if wanted to power off or not
# if check == "Yes": #if user enter Yes,>
#     os.system("shutdown /s /t 1") #,< it will shutdown theo device
# else: # if not
#     exit() #it will exit the program

# import cowsay
# cowsay.daemon("Hi Daemon")
# import pywhatkit ##py what kit module is imported
# pywhatkit.text_to_handwriting(""" this is a module which coverts
# text to hand
# writing.""", rgb=(0,0,255))
# print("\U0001F637") ### mask on emoji
# a = "rjamijghk"
# b = "ramijghk"
# print(a != b) #true bcoz they are diff vars with diff m-location

# pip install moviepy
# pip install ffmpeg
# import moviepy.editor as mp
# video = mp.VideoFileClip(r"sample.3gpp")
# video.audio.write_audiofile(r"output.mp3")

# from pytube import YouTube ### importing YouTube from pytube
# link = input("Enter the link ") # asking user to enter link
# print("Downloding...") # showing user that the process has started
# YouTube(link).streams.first().download() # main code to download Video
# print("Video downloaded successfully") # showing user that the video has downloaded

# import pyshorteners #pyshorteners module is imported
# url = input("Enter your url") #user will be asked to enter the url to be shortened
# s = pyshorteners.Shortener().arshorts.short(url) #this will short the link entered by user
# print("shorted link:", s) #it will print the link shorted by users

# import pyjokes #pyjokes module is imported
# print(pyjokes.get_joke()) #it will give you a joke only
# print(pyjokes.get_jokes()) #it will give you a list of jokes

# import webbrowser # importing webbrowser module
# from tkinter import * # importing tkinter

# root = Tk() # creating root
# root.title("WebBrowser") # setting GUI title
# root.geometry("300x200") # setting GUI geometry

# def zoom(): # function to open assignment.com in browser
#     webbrowser.open("www.zoom.us") #any url can be given here

# def google(): # function to open google in browser
#     webbrowser.open("www.google.com")

# zoom = Button(root, text="join the meeting", command=zoom).pack(pady=20) # button 2 call zoomfunc
# mygoogle = Button(root, text="open Google", command=google).pack(pady=20) # button to call google function

# root.mainloop()

# import webbrowser
# url = input('enter the url you want to open') #it will ask user to enter url
# webbrowser.open(url) #it will open the url entetred by user

# import os
# path = os.getcwd()
# for i in range(1,4): # you can set any range
#     os.mkdir(path + f"\\{i}") #it will create 3 new folders

# def convertToBinary(n): #function is created
#     if n>1: #if condition is setted
#         convertToBinary(n//2) #if condition matches, call that function with n divided by 2
#     print(n%2,end='') #print the remainder and with end='' so that the output will come in same line
# dec = 34 #dec number is given
# convertToBinary(dec) #called the function with arguement dec

# import itertools,random # simple program for cards
# deck = list(itertools.product(range(1,14),
# ['Spade','Heart','Diamond','Club']))
# random.shuffle(deck)
# print("you got: ")
# for i in range(5):
#     print(deck[i][0],'of',deck[i][1])

# from difflib import SequenceMatcher # a program to check plagiarism
# with open("shrtct.txt") as f1, open("temp.txt") as f2:
#     f1data=f1.read()
#     f2data=f2.read()
#     similarity=SequenceMatcher(None,f1data,f2data).ratio()
#     print(similarity*100)