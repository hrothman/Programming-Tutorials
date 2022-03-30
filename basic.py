##################################################################################################################################################################################################

#File Name: basic.py
#   Supplementary Files: main.py
#Basic Python Tutorial
#Author: Hayden Rothman
#Last Updated: 3/30/2022

#Table of Contents
#   -Basic file outline
#   -Variables
#   -Arithmetic
#   -Logical Operators
#   -Output
#   -Input
#   -Loops
#   -Functions
#   -Lists
#   -Summary
#   -Sample Project Ideas, answer for 1 is in main.py

##################################################################################################################################################################################################

#BELOW is the template python file, all new files will open with a
# functon named print_hi that takes a string variable and then prints
# that string along with Hi. We then have the main funtion, we do not
# touch line 1 but all lines below are free to edit
    #START of template file
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__': #Line 1 that we do NOT edit
    print_hi('dkdf')
    #END of template file

##################################################################################################################################################################################################

#variables
a = 'c' #this is a character, a single character from a keyboard input, any ascii value
b = "this is a string" #this is a string, a list of characters
c = 10 #this is an integer, all natural numbers within a particular range
d = 1.4 #this is a float or double depending on the size of the number, all real numbers within a particular range
e = True #this is a boolean value, T/F
    #there is many other default data types that a variable can be; you can also make custom data types using classes and objects
    # however that is more advanced and is covered in the intermediate.py file

##################################################################################################################################################################################################

#arithmetic using variables
temp1 = b + a #if you add a character and a string it will result in a string with the character added to the front or back
temp2 = c + d #if you add an integer and a double it will result in a double
#temp3 = b + c + e #if you add a number and non numerical value you will get an error
    #to get around this we convert data types, in this example we will convert all to string since b cannot be converted to numerical or boolean
temp3 = b + str(c) + str(e)

##################################################################################################################################################################################################

#Logical operators
if c == 10: #if is the start of this chain of comparisons, if this condition is satified is evaulated to true, then no other paths will be taken
    c = c + 1 #all lines within an if, elif, or else must be indented once in order to show they are within the statement
elif c < 10 or c >= 90 and c != 0: #elif requires a if before or an elif, but NOT required
    c = c - 1
else: #else requires an if before or an elif, but NOT required
    c = 0

##################################################################################################################################################################################################

#Output
print("this is a print statment")
print(13990)
print(e)
print(1+3+5 / 5)
print(2 != 5)
print("another thing", " my age is: ", 12, " i think?")

##################################################################################################################################################################################################

#Input
val = input("Enter your value: ")

##################################################################################################################################################################################################

#Loops and Iterating
for i in range(10):
    print(i)
for i in b:
    print(i)
for i in range(1,10):
    print(i)
i = 0
while i < 10:
    i = i + 1

##################################################################################################################################################################################################

#Defining Functions or methods (some languages use methods to refer to functions)
def functionName(functionInputs, input2 = 0):
    #body of function, almost any lines of code can be here
    return input2 + 1
    #functions can take any number (including 0) of variables of any type, they can also return any number (including 0) of any time of variables,
    #The variables functions take are its inputs and each input can be given a default value shown with input2 of functionName, the return values are its outputs
#Calling a function
functionName(10,1) #here we are calling functionName using 10 for functionInputs and 1 for input2
functionName(10) #in this case we are using the default value of 0 for input2

##################################################################################################################################################################################################

#Lists
ls = [] #this is an empty list
ls = [1,2,3] #a list must be made up of elements of the same type, however that type can be ANY type
ls = ["word"] #a list can be of any size
    # lists have built in functions you can access by using the dot opperator, .
ls.append("another word") #append adds the passed item to the end of the list
ls.remove("word")  #remove removes the passed item from the list, error if the item does not exist in the list
ls[0] #you can access elements of the list by using [] with the index of the item within the square brackets, INDEX START AT 0 (0 being the first element)
    #NOTE: lists can be multidimensional
ls = [ [1,2,3], [1], []]
ls[0][0]
ls.append([1,2])
ls.remove([1])
ls = ls + [[1,2]]
    #Now we understand lists, we can see that strings are simply a list of characters, understanding this makes dealing with strings far easier

##################################################################################################################################################################################################

#Summary:
    # Using these basic but incredible import building blocks you can build almost anything. There are many
    #  very important other aspects you must learn to by an expert however a strong fundation comes from
    #  understanding the above topics well.

##################################################################################################################################################################################################

#Sample Projects:
    #   1). Create a text analysiser that takes an input from the user and checks how many mistakes the user made,
    #       Solution: Shown in main.py, the check value is HA, and we loop so the user can input any length of HAHA '
    #                   the program will still work
    #   2). Create a simple task management program, start with a menu with options to view, edit, remove, and add tasks,
    #        from there add subscreens where you can do each item using simple user input and print statements

##################################################################################################################################################################################################