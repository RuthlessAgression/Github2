# try:
#     print('x') #it is correct
# except:
#     print('exception occured') #as above sts.is correct there is no exception and this block will not run
# else:
#     print('alright then') #hence, try block is correct without exception, else is used to print specific msg
# finally:
#     print('always run') #runs regardless of any block
#
# x = [3,4,5,]
# y = [3,4,5]
# print(x)
# z = x
# print(x is not z) #false coz z and x are same object
# print(x is not y) #true coz x and y are two diff. vars even though they have same values
# print(x != y) #false because x is equal to y coz they have same values

# a = [2,9,6]
# iterator = iter(a)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# b = 'lm10'
# x = iter(b)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# x = lambda a,b,c : a*b*c #same shit multiplied
# print(x(5,6,7))
# def myfunction(x): #myfunction(x) is defined at first
#     return lambda a : a * x #return lamda a such that a multiplies x
# dier = myfunction(2) #declared var'dier'which equals myfunction(2)
# trier = myfunction(3) # "     var'trier'           " my function(3)
# print(dier(11))
# print(trier(11)) #printed dier(11) and trier(11) to get ouput 22 and 33

