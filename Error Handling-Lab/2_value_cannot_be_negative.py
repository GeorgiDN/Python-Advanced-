class ValueCannotBeNegative(Exception):
    pass

for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative


######################################################################################  CONDITION  ##########################################################################################################################################
#2.	Value Cannot Be Negative
#Create your own exception called ValueCannotBeNegative.
# Write a program that reads five numbers from the console (on separate lines).
# If a negative number occurs, raise the exception.
#Input:
# 1
# 4
# -5
# 3
# 10

#Output
# Traceback (most recent call last):
#   File ".\value_cannot_be_negative.py", line 8, in <module>
#     raise ValueCannotBeNegative
# __main__.ValueCannotBeNegative
