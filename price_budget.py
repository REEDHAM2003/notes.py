budget=int(input("enter your budget\n "))
a=int(input("enter apple price\n "))
b=int(input("enter banana price\n "))
c=int(input("enter juice price\n "))
d=int(input("enter tomato price\n "))
add=a+b+c+d
print("the total is\n ",add)
if(budget>add):
    print("the remaining will be\n",budget-add)
elif(budget==add):
    print("no remainder")
else:
    print("you have to exceed budget")
if(budget-add>100):
    print("you are getting cheap price")
elif(add==budget):
    print("you can buy but no money remains")
elif(add<budget):  # we can use multiple elif's between if and else for the conditions we want 
    print("you are eligible to buy")
else:
    print("it is out of your budget")