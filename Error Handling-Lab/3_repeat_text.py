try:
    text = input()
    n_times = int(input())
    print(text * n_times)

except ValueError:
    print("Variable times must be an integer")


######################################################################################  CONDITION  ##########################################################################################################################################
#3.	Repeat Text
#Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
# If the user passes a non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".

#Input
#Hello
#Bye

#Output
#Variable times must be an integer

#Input
#Hello
#2


#Output
#HelloHello
