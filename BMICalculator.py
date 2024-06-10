# take user input for measurements
height = int(input('What is your height in inches? '))
weight = int(input('What is your weight in pounds? '))

# formula for BMI
bmi = (weight / (height ** 2)) * 703

# print output
print(bmi)