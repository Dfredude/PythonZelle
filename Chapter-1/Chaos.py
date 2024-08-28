# File: chaos. py 
# A simple program illustrating chaotic behavior. 
def main() : 
    print("This program7 illustrates a chaotic function") 
    X = eval(input("Enter a number between 0 and 1: ") ) 

    for i in range(10): 
        X = 3.9 * X * (1 - X) 
        print(X)
    
main() 