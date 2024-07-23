apple='''hey my name is reedham 
i study in jain university
my course is ECE'''
print(apple) 
print("\nlets use a for loop\n")
name="\nReedham\n"
for character in name: # this is used to automatically print index wise in this case reedham is 0-6 
    print(character)        # for can be used to print big sentances index wise without counting the letters in the string (character) is used

    for character in apple: #this is to write indexwise (vertically) the letter used in apple input string which is 'he my name is......'
        print(character)