number = 1
addup = 0
while number != 999:
    number = int(input('Enter a number to add up, enter 999 to quit: '))
    if number == 999:
        break
    addup += number
print(addup)
      