'''
Write a program that takes a number as input and prints 'Positive' if the number is positive, 'Negative' if it's negative, 
and 'Zero' if it's zero, but only if the number is an integer; if the number is not an integer, 
print 'Invalid input'?
'''

num = input("enter any nymbder: ")
if num.isdigit():
   num = int(num)
   if num>0:
      print("positive number")
   elif num<0:
      print("negative number")
   elif num==0:
      print("you entered zero")
else:
   print("invalid number")