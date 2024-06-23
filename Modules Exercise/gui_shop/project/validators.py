import re

from project.canvas import frame


def validate_password(password):
    password_criteria = [
        (r'.{6,}', "Password must be at least 6 characters long"),
        (r'[A-Z]', "Password must contain at least one uppercase letter"),
        (r'[a-z]', "Password must contain at least one lowercase letter"),
        (r'[0-9]', "Password must contain at least one digit"),
        (r'[@$!%*?&#_]', "Password must contain at least one special character: @$!%*?&#_")
    ]

    for pattern, error_message in password_criteria:
        if not re.search(pattern, password):
            x, y = 200, 225
            frame.create_text(
                x,
                y,
                text=error_message,
                fill="red",
                tags="error"
            )
            return False
    return True


def check_for_existing_username(users_data, info_dict):
    for user in users_data:
        if user["Username"] == info_dict["Username"]:
            frame.create_text(
                200,
                175,
                text=f"Username is already taken",
                fill="red",
                tags="error"
            )
            return True
    return False



# {'First Name': 'a', 'Last Name': 'a', 'Username': 'a', 'Password': 'Asd_12'}
# {'First Name': 'b', 'Last Name': 'b', 'Username': 'b', 'Password': 'Asd_13'}
# {'First Name': 'd', 'Last Name': 'd', 'Username': 'd', 'Password': 'Asd_15'}
