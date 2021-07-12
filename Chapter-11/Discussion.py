#D1
s1 = [2,1,4,3]
s2 = ['c', 'a', 'b']

print(s1+s2, 3*s1+2*s2, s1[1], s1[1:3], sep= '\n')
# s1 + s2[1] gives error, can't concatenate a list with a str

#D2
statements = [s1.remove(2), s1.sort(), s1.append([s2.index('b')]), s2.insert(s1[0], 'd')]
# s2.pop(s1.pop(2)) --> Out of index
for statement in range(4):
    s1 = [2,1,4,3]
    s2 = ['c', 'a', 'b']
    if statement == 0: s1.remove(2)
    elif statement == 1: s1.sort()
    elif statement == 2: s1.append([s2.index('b')])
    else: s2.insert(s1[0], 'd')
    print(s1, s2, sep= '\t')



