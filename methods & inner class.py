# class Student:

#     developer = 'AR10' #class variable

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3

#     @classmethod
#     def getdeveloper(cls):
#         return cls.developer #returns class variable without using objects

#     @staticmethod
#     def info():
#         print("This is irrespective of instance or class")

    # def get_m1(self):
    #     return self.m1
    #
    # def set_m1(self,value):
    #     self.m1 = value

# s1 = Student(34,47,32)
# s2 = Student(89,32,12)

# print(s1.avg())
# print(Student.getdeveloper())
# print(Student.info()) #or Student.info()
#
# inner class::
# class Student:

#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop() # is necessary while using inner class

#     def show(self):
#         print(self.name , self.rollno)
#         self.lap.show()

#     class Laptop: #inner class laptop is induced

#         def __init__(self):
#             self.brand = "Dell"
#             self.cpu = 'i5'
#             self.ram = 8

#         def show(self):
#             print(self.brand,self.cpu,self.ram)


# s1 = Student('AR',10)
# s2 = Student('RA',8)

# s1.show() #called the function show()

# lap1 = Student.Laptop() # is necessary to give object's attributes while using inner class

# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1)) # id no,>
# print(id(lap2)) # ,<is being checked
