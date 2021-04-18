import math
lengths = list(input("Enter 3 side legths of a triangle to obtain its area: "))
a,b,c= '', '', ''
print(lengths)
for i in range(len(lengths)):
    if lengths[i] is ',' :
        lengths = lengths[i+1:]
        break      
    else:
        a += str(lengths[i])

for j in range(len(lengths)):
    if lengths[j] is ',' :
        lengths = lengths[j+1:]
        break        
    else:
        b += str(lengths[j])

for l in range(len(lengths)):
    c += str(lengths[l])
     
print(a,b,c)
a,b,c = float(a), float(b), float(c) 
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('The area is ', area)