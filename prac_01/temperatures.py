def main():

    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit1 = float(input("Fahrenheit: "))
            celsius1 = 5 / 9 * (fahrenheit1 - 32)
            print("Result: {:.2f} C".format(celsius1))
        else:
            print("Invalid option")
            print(menu)
            choice = input(">>> ").upper()
    print("Thank you.")


main()