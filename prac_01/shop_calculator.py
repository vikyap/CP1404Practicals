def main():
    items = int(input("Enter number of items: "))
    total_price = 0
    while items < 0:
        print("Invalid number of items!")
        items = int(input("Enter number of items: "))
    if items > 0:
        for i in range(items):
            price = float(input("Enter price of item: "))
            total_price += price
        if total_price > 100:
            total_price = total_price * 0.90
    print("Total price for", items, "items is", total_price)


main()
