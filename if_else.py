a=int(input("enter your age\n"))
print("your age is:",a )
if(a>18):
    print("you can drive")
else:
    print("you cannot drive")    
# if the expression is true it will execute the code of if otherwise it will execute for else
# conditional operators
# (>,<,>=,<=,==,!=)  these are conditional operators
#conditional operators
print(a>18) # greater then
print(a<18) # less than
print(a>=18) # greater than or equal to 
print(a<=18) # less than or equal to 
print(a==18) # is equal to 
print(a!=18) # not equal to 
#voting system using if else
b=int(input("enter your age: "))    
print("your age is: ",b)
if(b>=18): # semicolon is necesarry
    print("you can vote") #the space before print is indentation indicating that we have entered the block of if 
else:
    print("you cannot vote")  #the space before print is and indentation indicating that we have entered the block if else
print("yay")   # this is not and indentation therefore it will print in both condition it is a normal string 
# price chechking and adding to cart code using python
price=210
budget=200
if(price<=budget):
    print("alexa add to cart")
else:
    print("alexa remove from cart")