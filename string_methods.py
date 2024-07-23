#strings are immutable- they cannot change
a="!!Reedham !!!!!!!! Reedham!!!"
print(len(a)) #this is used to identify the length of the string
print(a.upper()) #this is used to change the string to upper case
print(a.lower()) #this is used to convert the string to lower case 
print(a.rstrip("!")) #this is used to strip out what we want in this we have stripped out "!" only trailing char
print(a.rstrip("!")) #this is used to strip out special char of ending only
print(a.replace("Reedham","manish")) # this is used to replace the string al the string occurences
print(a.split(" ")) # the string must have space to split 
title="introduction to python"
print(title.capitalize()) #used to capitalize example changing the first letter of title to capital
title1="introduCtion to PyThOn"
print(title1.capitalize()) # capitalize is also used to rectify the errors of capital letters in between the sentance changing first to capital
                           # and others to lower
str1="welcome to python"   #we will use this string to centralize it 
print(len(str1))           # finding out the length of this string                
print(str1.center(50))     # here the string name.centre(50) is used to centralize the string
print(len(str1.center(50))) # here we are measuring the length of the string after cetralizing it 
b="reedham!!!!reedham!!!!!manish!!!!!manish!!!!manish!!!!maisuriya"
print(b.count("reedham"))  #stringname.count("  ") is used to count how many times the word has appeared
print(b.count("manish")) # here we are counting how many times manish has appeared
print(b.count("maisuriya")) # here we are counting how many times maisuriya has appeared
str2="welcome to python!!" 
print(str2.endswith("!!")) #to check weather the string is ending with that certain character
print(str2.endswith("??")) # here we cheack str2 ends with ? or not it will give false
print(str2.endswith("to",4,10)) #check weather the char in str2 between 4-10 end with to
print(str2.endswith("to",5,9)) # checking weather ends with to from 5-9
str3="he's name is ree. ree is a goodboy"
print(str3.find("is")) # finds at which index number that word is ther in the string of the first occurence
print(str3.find("ishh")) # this will return -1 because it is not there
print(str3.find("is")) # index is also used to find the word in the string
str4="My name is reedham born on 21 02 2003"
print(str4.isalnum()) #isalnum will show true if the string has A-Z a-z 0-9 and false for other char and spaces for str4 it will be false
str5='IAMREEDHAMree21'
print(str5.isalnum())# isalnum function will give true 
print(str5.isalpha()) #isalpha will give true if our string has A-Z a-z and false if it has numbers
str6="reedham"
print(str6.islower()) # this will give true if the string is made of lowercase letters and flase if there is uppercase
str7="we wish you happy diwali"
print(str7.isprintable()) # this will show if the string is printable or not and if it goes to \n then it is false
print(str7.isspace()) # true only for white spaces (full of white spaces)
str7="          "
print(str7.isspace()) # this will give true as it has white
str7="Reedham Manish Maisuriya"
print(str7.istitle()) # returns true if each word first letter is capital otherwise false
str7="WORLD HEALTH ORGANIZATION"
print(str7.isupper()) # returns true if the string is in uppercase otherwise false
str7="This Is not Title"
print(str7.istitle()) # returns false beacuse all words dont have first letter as capital 
str7="Reedham is may name"
print(str7.startswith("Reedham")) #will give true if the string is starting with reedham otherwise false 
print(str7.startswith("name")) # will give false because the string does not start with name 
str7="Reedham is My Name"
print(str7.swapcase()) # this will change uppercase to lowercase and viceversa
str7="His name is ree\nhe is a goodboy"
print(str7.title()) # changes the string to a title- by changing all first letters to capital