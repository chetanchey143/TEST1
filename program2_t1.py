'''
Write a program that takes a number as input and prints ' vegetarian' if number is divisiable by 5, 
'non-vegetarian' if number is divisiable by 10?
'''

num=input("enter a number: ")
if num.isdigit():
    num=int(num)
    if(num%5==0):
        print("vegeterian")
    elif(num%10==0):
        print("non veg")
    elif(num%5==0 and num%10==0):
        print("vegan")
else:
    print("invalid input")