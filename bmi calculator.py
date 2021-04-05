weight_kg = input('What is your weight in kilograms? ')
height_m = input('What is your height in metres? ')
n_weight = float(weight_kg)
n_height = float(height_m)
bmi_calc = n_weight/(n_height*n_height)
answer = f'Your weight is {weight_kg} kg and your height is {height_m} m,hence your BMI is {bmi_calc}.'
print(answer)

if bmi_calc > 23.0:
    print('You need to eat less and workout more, you fat phuck.')
elif bmi_calc < 19.0:
    print ('EAT MORE, u scrawny bastard.')
else:
    print ('Good job!')
