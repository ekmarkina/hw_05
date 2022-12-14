def get_password():
    password = input("Введите пароль: ")
    if (
        len(password) >= 6 and
        any(char.isdigit() for char in password) and
        any(char.isalpha() for char in password) and
        "password" not in password.lower()
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    result = get_password()
    print(result)
