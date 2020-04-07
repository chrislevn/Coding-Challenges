# Check if the value is a jumping number or not
def checkJumping(value):

    #Split number into a list of string
    splitNumber = list(str(value))

    # Take first and second values and convert them into integer
    firstValue = int(splitNumber[0])
    secondValue = int(splitNumber[1])

    # Calculate difference between the second and the first value
    diff = secondValue - firstValue

    # Based on the trend of the first 2 values, define whether the trend is increasing or not
    if diff > 0:
        increasing = True
    elif diff == 0:
        return False
    else:
        increasing = False

    # Define the trend from the second value
    if increasing:
        # Reversed loop
        for i in range(len(splitNumber) - 1, 1, -1):
            diff = int(splitNumber[i]) - int(splitNumber[i-1])

            # if diff < 0, mean the trend is different. Therefore, the value is a jumping number
            if diff < 0:
                return True
    else:
        # Reversed loop
        for i in range(len(splitNumber) - 1, 1, -1):
            diff = int(splitNumber[i]) - int(splitNumber[i-1])

            # if diff > 0, mean the trend is different. Therefore, the value is a jumping number
            if diff > 0:
                return True
    return False


count = 100

# create a realCounter variable to check if the sequence has total 500 numbers
realCounter = 0

# Result value
total = 0

# Create a sample test array to check if the sequence is a list of jumpy numbers or not
# testArr = []

# Run the loop from 100, the loop stops when the sequence has total 500 numbers.
while realCounter < 500:
    if checkJumping(count):

        # testArr.append(count)
        realCounter += 1

        total += count

    count += 1

# print(testArr)
print(total)