from prac_08.taxi import Taxi


def main():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print("Taxi details:", new_taxi)
    print("Payable fare is: $", new_taxi.get_fare())
    new_taxi.start_fare()
    new_taxi.drive(100)
    print("Taxi details:", new_taxi)
    print("Payable fare is: $", new_taxi.get_fare())


main()
