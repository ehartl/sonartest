def check_password_strength(password: str) -> None:
    if len(password) < 8:
        print("Password does not meet requirements.")
        return

    has_upper = has_lower = has_digit = has_special = False
    special_characters = "!@#$%&"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Valid Password.")
    else:
        print("Password does not meet requirements.")
