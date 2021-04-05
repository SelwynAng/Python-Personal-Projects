weight = int(input('What is your weight? '))
unit = input('In (L)bs or (k)g? ')

if unit == 'L' or unit == 'l':
    weight_final = weight * 0.453
    print(f'Your weight in kilograms is {weight_final}.')
elif unit == 'K' or unit == 'k':
    weight_final = weight / 0.453
    print(f'Your weight in pounds is {weight_final}.')
else:
    print('Incorrect expression for 2nd question. Try again.')
