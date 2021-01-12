from prac_08.silverservicetaxi import SilverServiceTaxi


def main():
    fancy1 = SilverServiceTaxi("Hummer", 100, 4)
    fancy2 = SilverServiceTaxi("BMW", 100, 2)
    fancy1.drive(40)
    fancy2.drive(18)
    print(fancy1, "\nPayable fare is: ${}".format(fancy1.get_fare()))
    print(fancy2, "\nPayable fare is: ${}".format(fancy2.get_fare()))


main()
