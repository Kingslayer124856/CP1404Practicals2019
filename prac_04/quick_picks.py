import random

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Really, No try again")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
