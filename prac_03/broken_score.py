import random

def check_score(score):
    if score < 0 or score > 100:
        return False
    else:
        if score < 50:
            result = 1
        elif score >= 50 and score <= 89:
            result = 2
        elif score >= 90 and score <= 100:
            result = 3
    return result


def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    if result == 1:
        print("Bad")
    elif result == 2:
        print("Passable")
    elif result == 3:
        print("Excellent")
    while not check_score(score):
        print("Invalid score!")
        score = float(input("Enter score: "))

    score = random.randint(0, 100)
    print("Random score is:", score)
    result = check_score(score)
    if result == 1:
        print("Bad")
    elif result == 2:
        print("Passable")
    elif result == 3:
        print("Excellent")


main()




