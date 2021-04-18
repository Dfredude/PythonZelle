def ants_march_verse(number_of_ants):
    return 'The ants go marching {0} by {0},'.format(number_of_ants)

def ants_march_first_verses(number_of_ants):
    verses = ants_march_verse(number_of_ants) + ' hurrah! hurrah!'
    return verses

def little_one(action):
    return 'The little one stops to {0}'.format(action)

def finish():
    return'''And they go al marching down...
In the ground...
To get out...
Of the rain.
Boom! Boom! Boom!'''

def main():
    little_one_doing = ['suck his thumb', 'tie his shoe', 'check the time', 'see his mom', 'look the sky', 'take a call',
    'kiss his wife', 'see a fly', 'hear music', 'watch GOT']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for i in range(10):
        number = numbers[i]
        print(ants_march_first_verses(number))
        print(ants_march_first_verses(number))
        print(ants_march_verse(number))
        print(little_one(little_one_doing[i]))
        print(finish())
        print()
main()