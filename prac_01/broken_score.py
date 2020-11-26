def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score < 50:
            print("Bad")
        elif score >= 50 and score <= 89:
            print("Passable")
        elif score >= 90 and score <= 100:
            print("Excellent")


main()
