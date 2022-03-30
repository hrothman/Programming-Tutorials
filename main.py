##################################################################################################################################################################################################

#File Name: main.py
#Basic Python Tutorial Supplementary File 1
#Author: Hayden Rothman
#Last Updated: 3/30/2022

#   Here we have a very simple program that will ask the user to input HAHAHAH has many times as they can without making a mistake, it
#     will then analysis the users input and will output (the number of characters inputted correctly, if the input was flawless,
#     the input minus the first instance of a mistake)


##################################################################################################################################################################################################

def hahaha(str):
    wasH = True
    wasA = True
    str2 = ""
    counter = 0
    for u in str:
        if u == 'H' and wasA:
            wasA = False
            wasH = True
        elif u == 'A' and wasH:
            wasH = False
            wasA = True
        else:
            return counter, counter == len(str), str2
        str2 += u
        counter += 1 #this is the same as counter = counter + 1
    return counter, counter == len(str), str2


if __name__ == '__main__':
    g = input("Enter a HAHAHAHAHAHAHAH as many times as you can without making a mistake:")
    a,b,c = (hahaha(g))
    if b:
        print("    Congratulations you typed ", a, " characters flawlessly")
    else:
        print("    you typed ", a, " characters before a mistake was made")
    print("  your flawless input: ", c)
    input("\n\n\n           press any key to close")
