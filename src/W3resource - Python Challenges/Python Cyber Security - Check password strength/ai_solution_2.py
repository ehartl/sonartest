def check_password_strength(password: str) -> None:
    if len(password) < 8:
        print("Password does not meet requirements.")
        return

    special_characters = set("!@#$%&")
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_characters for c in password)

    if has_upper and has_lower and has_digit and has_special:
        print("Valid Password.")
    else:
        print("Password does not meet requirements.")
