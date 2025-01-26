class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


SPECIAL_CHARACTERS = {"@", "*", "&", "%"}


def check_for_empty_space(password):
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")


def check_password_length(password, min_password_length=8):
    if len(password) < min_password_length:
        raise PasswordTooShortError("Password must contain at least 8 characters")
        # raise PasswordTooShortError(f"Password must contain at least {min_password_length} characters") # dynamic password_length


def check_password_is_too_common(password):
    if password.isdigit() or password.isalpha() or all(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordTooCommonError(
            "Password must be a combination of digits, letters, and special characters"
        )


def check_for_special_character(password):
    if not any(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordNoSpecialCharactersError(
            "Password must contain at least 1 special character"
        )


def is_valid_password(password):
    check_for_empty_space(password)
    check_password_length(password)
    check_password_is_too_common(password)
    check_for_special_character(password)

    return True


def main():
    while True:
        password = input()
        if password == "Done":
            break

        if is_valid_password(password):
            print("Password is valid")


if __name__ == "__main__":
    main()


########################################################################################################################

# class PasswordTooShortError(Exception):
#     pass
#
#
# class PasswordTooCommonError(Exception):
#     pass
#
#
# class PasswordNoSpecialCharactersError(Exception):
#     pass
#
#
# class PasswordContainsSpacesError(Exception):
#     pass
#
#
# SPECIAL_CHARACTERS = {"@", "*", "&", "%"}
#
#
# def is_valid_password(password):
#     if " " in password:
#         raise PasswordContainsSpacesError("Password must not contain empty spaces")
#
#     if len(password) < 8:
#         raise PasswordTooShortError("Password must contain at least 8 characters")
#
#     if password.isdigit() or password.isalpha() or all(char in SPECIAL_CHARACTERS for char in password):
#         raise PasswordTooCommonError(
#             "Password must be a combination of digits, letters, and special characters"
#         )
#
#     if not any(char in SPECIAL_CHARACTERS for char in password):
#         raise PasswordNoSpecialCharactersError(
#             "Password must contain at least 1 special character"
#         )
#
#     return True
#
#
# def main():
#     while True:
#         password = input()
#         if password == "Done":
#             break
#
#         if is_valid_password(password):
#             print("Password is valid")
#
#
# main()
