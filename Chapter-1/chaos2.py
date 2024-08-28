def main():
    print("This program illustrates the chaotic function x= 3.9*x*(1-x)") #Introduction
    #Input and assignment
    x = float(input("First enter a number between 0 and 1(This will be x in our equation): "))  
    y = float(input("""Now enter a different number between 0 and 1(This will be another x
used to contrast both variable results: """)) #"   "
    n = int(input("How many iterations do you want:"))  #"  "
    print('index', x,y,sep='\t\t')
    print('---------------------------------------------')
    for i in range(n): #Loop for n times
        x = 3.9*x*(1-x) 
        y = 3.9*x*(1-x)
        print(i+1, round(x, 5), round(y, 5), sep='\t\t')
    print(input('Press Enter to exit'))

main()
