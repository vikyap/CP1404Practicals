def c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def f_to_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def main():

    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(c_to_f(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print("Result: {:.2f} C".format(f_to_c(fahrenheit)))
        else:
            print("Invalid option")
            print(menu)
            choice = input(">>> ").upper()
    print("Thank you.")


main()