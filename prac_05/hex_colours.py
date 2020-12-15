def main():
    colour_code = {"deepskyblue1": "#00bfff", "deepskyblue2": "#00b2ee", "deepskyblue3": "#009acd",
                   "deepskyblue4": "#00688b", "dimgray": "#696969", "dodgerblue1": "#1e90ff",
                   "dodgerblue2": "#1c86ee", "dodgerblue3": "#1874cd", "dodgerblue4": "#104e8b"}
    colour_name = input("Enter a colour: ")
    while colour_name != "":
        if colour_name in colour_code:
            print(colour_code[colour_name])
        else:
            print("Invalid colour")
        colour_name = input("Enter a colour: ")



main()
