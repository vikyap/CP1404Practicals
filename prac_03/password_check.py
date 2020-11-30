def main():
    password = get_password()
    print_password(password)


def get_password():
    print("Password must have minimum of 10 characters")
    password = input("Enter a password: ")
    min_length = 10
    while len(password) < min_length:
        print("Password is too short")
        password = input("Enter a password: ")
    if len(password) >= min_length:
        print("Password is accepted")
    return password


def print_password(password):
    for i in range(len(password)):
        print("*", end=' ')


main()
