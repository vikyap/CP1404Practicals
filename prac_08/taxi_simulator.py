from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi


def taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def main():
    bill_to_date = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    user_choice = input(">>> ")
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available:")
            print(taxi_list(taxis))
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif user_choice == "d":
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            fare = current_taxi.get_fare()
            print("Your {} trip cost you ${}".format(current_taxi.name, fare))
            bill_to_date += fare
        print("Bill to date: ${}".format(bill_to_date))
        print(menu)
        user_choice = input(">>> ").lower()
    print("Total trip cost: ${}".format(bill_to_date))
    print("Taxis are now:")
    print(taxi_list(taxis))


main()









