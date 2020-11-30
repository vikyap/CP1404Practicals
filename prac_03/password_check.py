min_length = 10


def main():
    print("Password must have a minimum of 10 characters")
    password = input("Enter a password: ")
    get_password(password)
    while not get_password(password):
        print("Password is too short")
        password = input("Enter a password: ")
        print_password(password)


def get_password(password):
    if len(password) >= min_length:
        return True


def print_password(password):
    for i in range(len(password)):
        print("*", end=' ')


main()
