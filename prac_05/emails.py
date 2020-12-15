def name_from_email(email):
    username = email.split("@")[0]
    parts = username.split(".")
    name = " ".join(parts).title()
    return name


def main():
    email_name = {}
    email = input("Enter your email: ")
    while email != "":
        name = name_from_email(email)
        correct = input("Is your name {}? (Y/N): ".format(name)).upper()
        if correct.upper() == "N" or correct != "":
            name = input("Enter your name: ")
        email = input("Enter your email: ")
        email_name[email] = name
    for email, name in email_name.items():
        print("{} ({})".format(name, email))


main()
