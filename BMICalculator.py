# function to call all other functions
def main():
    bmi = calculateBMI()
    printBMI(bmi)

# take user input for measurements
def getMeasurements(prompt = 'Enter number: '):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except ValueError:
            print('Invalid input. Please enter a valid number.')

# formula for BMI
def calculateBMI():
    height = float(getMeasurements('What is your height in inches?\n'))
    weight = float(getMeasurements('What is your weight in pounds?\n'))
    
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

# call main
main()
