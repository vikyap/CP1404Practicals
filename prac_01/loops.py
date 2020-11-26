def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print(" ")
    print("Count in 10s")
    for i in range(0, 101, 10):
        print(i, end=' ')
    print(" ")
    print("Count down from 20 to 1")
    for i in range(20, 0, -1):
        print(i, end=' ')
    print(" ")
    stars = int(input("Number of stars: "))
    for i in range(stars):
        print("*", end=' ')
    print(" ")
    print("Increasing stars")
    for i in range(stars):
        for x in range(0, i + 1):
            print("*", end=' ')
        print(" ")


main()
