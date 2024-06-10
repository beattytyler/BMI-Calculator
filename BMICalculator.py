# function to use all other functions
def main():
    height, weight = getMeasurements()
    bmi = calculateBMI(height, weight)
    printBMI(bmi)

# take user input for measurements
def getMeasurements():
    while True:
        try:
            height = float(input('What is your height in inches?\n'))
            weight = float(input('What is your weight in pounds?\n'))
            return height, weight
        except ValueError:
            print('Invalid input. Please enter a valid number.')

# formula for BMI
def calculateBMI(height, weight):
    bmi = (weight / (height ** 2)) * 703
    return bmi

# print output
def printBMI(bmi):
    # convert bmi to string and round to once decmial place
    bmi_str = str(round(bmi, 1))
    print('Your BMI is: ' + bmi_str)

    # classification for bmi range
    if bmi < 19:
        print('You are underweight.')

    elif 19 < bmi < 24:
        print('You are in the optimal range.')

    elif 24 < bmi < 30:
        print('You are overweight.')

    elif 30 < bmi < 35:
        print('You have class I obesity.')

    elif 35 < bmi < 40:
        print('You have class II obesity.')

    elif bmi > 40:
        print('You have class III obesity.')

# run program
main()
