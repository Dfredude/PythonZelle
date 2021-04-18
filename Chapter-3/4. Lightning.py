print('''This program will let you know how far from you a lightning strike is by knowing the difference of time
between the appearence of the strike and the arrival of the sound to your ear''')
time = float(input('Enter the time it took the sound of a lightning strike to reach you: '))
distance = time*1100
if distance >= 5280:
    final_distance = distance/5280
    print('The distance is ', final_distance, 'miles')
else:
    print('The distance is ', distance, 'feet')