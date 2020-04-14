import numpy as np
import time

# State the fact
NUM_OF_DIGITS = 3
MIN_NUM = 000
MAX_NUM = 999
FACT1 = "All digits are wrong"
FACT2 = "1 digit is right and in the right place"
FACT3 = "1 digit is right but in the wrong place"
FACT4 = "2 digit are correct but in the wrong place"
FACT5 = "1 digit is right but in the wrong place 2"

pairs = {FACT3: 147, FACT2: 189, FACT4: 964, FACT1: 523, FACT5: 286}


# Check if all digits in list @guess_dig is not in string @num

def chekcDigNotIn(guess_dig, num):
    tempDig = [int(i) for i in str(num)]
    for x in guess_dig:
        for y in tempDig:
            if x == y:
                return False
    return True


# Check FACTS with string @guess and string @num
def checkFact1(guess, num):
    guess_dig = [int(i) for i in str(guess)]
    return chekcDigNotIn(guess_dig, num)


def checkFact2(guess, num):
    tempDig = [int(i) for i in str(num)]
    guess_dig = [int(i) for i in str(guess)]
    for i in range(NUM_OF_DIGITS):
        if guess_dig[i] == tempDig[i]:
            pop_list = guess_dig.copy()
            pop_list.pop(i)
            if chekcDigNotIn(pop_list, num):
                return True
    return False


def checkFact3(guess, num):
    tempDig = [int(i) for i in str(num)]
    guess_dig = [int(i) for i in str(guess)]
    for i in range(NUM_OF_DIGITS):
        if guess_dig[i] in tempDig:
            guessClone = guess_dig.copy()
            tempClone = tempDig.copy()
            guessClone.pop(i)
            tempClone.pop(i)
            if chekcDigNotIn(guessClone, num):
                if guess_dig[i] in tempClone:
                    return True
    return False


def checkFact4(guess, num):
    tempDig = [int(i) for i in str(num)]
    guess_dig = [int(i) for i in str(guess)]
    for i in range(NUM_OF_DIGITS - 1):
        if guess_dig[i] in tempDig:
            for j in range(i + 1, NUM_OF_DIGITS):
                if guess_dig[j] in tempDig:
                    guessClone = guess_dig.copy()
                    guessClone.pop(i)
                    guessClone.pop(j - 1)
                    if chekcDigNotIn(guessClone, num):
                        tempClone1 = tempDig.copy()
                        tempClone2 = tempDig.copy()
                        tempClone1.pop(i)
                        tempClone2.pop(j)
                        if guess_dig[i] in tempClone1 and guess_dig[j] in tempClone2:
                            return True
    return False


def guess():
    guess = MIN_NUM
    while (int(guess) <= MAX_NUM):
        guess = str(guess).zfill(NUM_OF_DIGITS)
        if checkFact1(guess, pairs[FACT1]) and checkFact2(guess, pairs[FACT2]) and checkFact3(guess, pairs[
            FACT3]) and checkFact4(guess, pairs[FACT4]) and checkFact3(guess, pairs[FACT5]):
            print(guess)
        guess = int(guess) + 1


guess = 679
print(checkFact1(guess,pairs[FACT1]),checkFact2(guess,pairs[FACT2]),checkFact3(guess,pairs[FACT3]),checkFact4(guess,pairs[FACT4]),checkFact3(guess,pairs[FACT5]))

start_time = time.time()
guess()
print("--- %s seconds ---" % (time.time() - start_time))

# TODO: - Enhance guess input from FACT4
#       - Code only work for number with distinc digits. FIGURE HOW TO FIX THIS!

# def check():
#     print(dig_list)

# # remove all the digits of a number @num from the given list @list
# def removeWrongDig(num, list) :
#     rem_list = [int(i) for i in str(num)]
#     for dig in rem_list:
#         remWrongDig(dig,list)

# # remove digit @dig from the given list @list
# def remWrongDig(dig, list):
#     if dig in list:
#             list.remove(dig)

# def guessFromF4(pairs) :
#     for i in range(3):
#         guess_list = [int(i) for i in str(pairs[FACT4])]
#         rem_list = []
#         rem_num = guess_list.pop(i)
#         rem_list.append(rem_num)

#         for i in range(3):
#             for num in pairs[FACT3]:
#                 compare_list = [int(i) for i in str(num)]
#                 if (set(guess_list) & set (compare_list)):
#                     print(guess_list,compare_list)