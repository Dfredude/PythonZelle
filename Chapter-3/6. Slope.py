values = list(input("What are the two point in plane? Use the order x1,x2,y1,y2 and comma to separate the values as well : "))
x1,x2,y1,y2= '', '', '', ''
print(values)
for i in range(len(values)):
    if values[i] is ',' :
        values = values[i+1:]
        print(values)
        break      
    else:
        x1 += str(values[i])

for j in range(len(values)):
    if values[j] is ',' :
        values = values[j+1:]
        print(values)
        break        
    else:
        x2 += str(values[j])

for k in range(len(values)):
    if values[k] is ',' :
        values = values[k+1:]
        break    
    else:
        y1 += str(values[k])

for l in range(len(values)):
    y2 += str(values[l])
     
print(x1,x2,y1,y2)
x1,x2,y1,y2 = float(x1), float(x2), float(y1), float(y2)  
slope = (y2-y1)/(x2-x1)
print('The slope is ', slope)