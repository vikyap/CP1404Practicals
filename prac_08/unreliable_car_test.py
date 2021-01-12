from prac_08.unreliable_car import UnreliableCar


def main():
    car1 = UnreliableCar("Reliable", 100, 99)
    car2 = UnreliableCar("Useless", 100, 10)
    print("Drive distance 20km")
    print("{} drove {}km".format(car1.name, car1.drive(20)))
    print("{} drove {}km".format(car2.name, car2.drive(20)))
    print("Drive distance 50km")
    print("{} drove {}km".format(car1.name, car1.drive(50)))
    print("{} drove {}km".format(car2.name, car2.drive(50)))
    print(car1)
    print(car2)


main()


