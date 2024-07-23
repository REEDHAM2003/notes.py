name="reedham,manish,maisuriya"
print(name[0:7]) 
''' slicing and printing the string we use square bracket then the index number of a char to n-1 index number of where we want to end '''
#in the above case reedham has index number from 0-6 therefore to print reedham we use [0:7]
print(len(name)) #len is used to know the amount of characters in the string
len1=len(name) #here we use len1 and we give it len function for the string name to store how many char name has(len means length)
print('name has',len1,'letters in it') #here we are using the stored length in len to print the number of char in name
print(name[0:3]) #this will print ree since r-0 e-1 e-2 and we use n-1 
print(name[0:5]) #this will give reedh which is 0-4 but we use 5 since we have to use n-1 
print(name[0:-21]) #this we get ree since pythin will itself keep len(name) before -21 below is the example
print(name[0:len(name)-21] )
print(name[:2]) #if i dont keep zero python automaticallty takes zero
fruit="mango"
print(fruit[-3:-1]) #this will print ng since 5-3 is 2 and at 2 we haven and 5-1 is 4 but we use n-1 so it will print g which is at 3 
quiz="harry"
print(quiz[-4:-2])