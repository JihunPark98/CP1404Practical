import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    numPick = int(input("How many quick picks? "))
    while numPick < 0:
        print("Invalid")
        numPick = int(input("How many quick picks? "))

    for i in range(numPick):
        pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in pick:
                number = random.randint(MINIMUM, MAXIMUM)
            pick.append(number)
        pick.sort()
        print(pick)

main()