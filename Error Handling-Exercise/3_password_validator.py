class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


SPECIAL_CHARACTERS = {"@", "*", "&", "%"}


def is_valid_password(password):
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isdigit() or password.isalpha() or all(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordTooCommonError(
            "Password must be a combination of digits, letters, and special characters"
        )

    if not any(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordNoSpecialCharactersError(
            "Password must contain at least 1 special character"
        )

    return True


def main():
    while True:
        password = input()
        if password == "Done":
            break

        if is_valid_password(password):
            print("Password is valid")


main()
