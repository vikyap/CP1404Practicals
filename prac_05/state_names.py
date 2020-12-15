def main():
    code_to_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                    "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria",
                    "TAS": "Tasmania"}
    print(code_to_name)
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in code_to_name:
            print(state_code, "is", code_to_name[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    for state_code, state_name in code_to_name.items():
        print("{:3} is {}".format(state_code, state_name))


main()
