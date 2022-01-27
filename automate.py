# spamming normally
# import pyautogui # type pip install pyautogui in cmd or terminal
# import time #time module is imported
# msg = 40 # instead of 5 any number can be given, it will send 5 auto messages
# while msg > 0: #while loop is initialized
#     time.sleep(1) #1 s only before msg
#     pyautogui.typewrite(''' !! 🤣🤦‍♂️😒👀😁😎🤣🤦‍♂️😒👀😁😎''')
#     time.sleep(1) #1s after prev. msg
#     pyautogui.press("enter")
#     msg -= 1 #msg = msg - 1pya goes like 5,4,3,2,1

# from ctypes.wintypes import WORD
# ### spamming by reading file
# import pyautogui, time
# time.sleep(1)
# with open("ar.json", "r") as f:
#     for word in f:
#         pyautogui.typewrite(word)
#         pyautogui.press("enter")

### importing whole module
# from tkinter import *
# from tkinter.ttk import *

# from datetime import datetime
# from time import strftime # importing strftime function to retrieve system's time
## creating tkinter window
# root = Tk()

# root.title('Auto Digital Clock')
## This function is used to display time on the label

# def time():

#     string = strftime('%Y/%m/%d %I:%M:%S')
#     lbl.config(text=string)
#     lbl.after(1000, time) 
## Styling the label widget so that clock will look more attractive

# lbl = Label(root, font=("ds-digital", 50, "bold"),
#             background = "black",
#             foreground = "green")
# # Placing clock at the centre of the tkinter window

# lbl.pack(anchor = 'center')
# time()

# mainloop()

### downloading profile data from instagram
# import instaloader #firstly, you need to install this module
# insta = instaloader.Instaloader()
# acc = "abishek_regmi"
# insta.download_profile(acc, profile_pic_only=False) #it will download everything from insta profile along with pp

### creating sketch img from normal img
# import cv2
# image = cv2.imread("C:\\Users\\User\\Pictures\\dwn.png")
# grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# invert = cv2.bitwise_not(grey_img)
# blur = cv2.GaussianBlur(invert, (21,21),0)
# invertedblur = cv2.bitwise_not(blur)
# sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# cv2.imwrite("sketch.png", sketch)

### text reader::
# import pyttsx3
# friend = pyttsx3.init()
# speech = input("write sth:") #user is allowed to write whatever he want to be heard 
# friend.say(speech)
# # friend.say("hello AR1o") #incase you dont wanna give user a chance try it
# friend.runAndWait()

# import pyttsx3 
# import PyPDF2 #both modules are to be downloaded at fisrt
# book = open("book_name.pdf","rb") #the pdf file you want it to read is to be opened now
# pdfReader = PyPDF2.PdfFileReader(book) #it will read that opened book
# pages = pdfReader.numPages #it will count num of pages in that book
# print(pages) #it will print the num of pages
# speaker = pyttsx3.init() #we have initialized txt to speech py module
# for num in range(1, pages): 
# #for loop is used to iterate through all pages from first to last
# note:: you can start from any other page except page 1
#     page = pdfReader.getPage(1) #it will start from first page
#     text = page.extractText() #will extract it 
#     speaker.say(text) #then it will start speaking
#     speaker.runAndWait() #we have to run and wait until file is readen

# pyttsx3 with voice ,rate, id arrangement
# # import pyttsx3
# engine = pyttsx3.init() # object creation

# # """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# # """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# # engine.save_to_file('Hello World', 'test.mp3')
# # engine.runAndWait()