year = int(input("Enter a year to determine the Gregorian epact: "))
C = year//100
epact = ((8+(C//4))-C+((8*C+13)//25)+11*(year%19))%30
print(epact)