class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()

    if email == "End":
        break

    name = email.split("@")[0]
    domain = email.split(".")[-1]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.count("@") != 1:
        raise MustContainAtSymbolError("Email must contain @")

    if domain not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")


######################################################################################  CONDITION  ##########################################################################################################################################

# 2.	Email Validator
# You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:
# •	NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
# •	MustContainAtSymbolError - raise it when there is no "@" in the email
# •	InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
# When an error is encountered, raise it with an appropriate message:
# •	NameTooShortError - "Name must be more than 4 characters"
# •	MustContainAtSymbolError - "Email must contain @"
# •	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one

# Input:
# abc@abv.bg

#Output
# Traceback (most recent call last):
#   File ".\email_validator.py", line 20, in <module>
#     raise NameTooShort("Name must be more than 4 characters")
# __main__.NameTooShort: Name must be more than 4 characters


# Input:
# peter@gmail.com
# petergmail.com

#Output
# Email is valid
# Traceback (most recent call last):
#   File ".\email_validator.py", line 18, in <module>
#     raise MustContainAtSymbolError("Email must contain @")
# __main__.MustContainAtSymbolError: Email must contain @


# Input:
# peter@gmail.hotmail

#Output
# Traceback (most recent call last):
#   File ".\email_validator.py", line 22, in <module>
#     raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
# __main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net
