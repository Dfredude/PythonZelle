def main():
    print("This program computes the average of any amount exam scores.")
    scores = []
    scores = (eval(input("Enter scores separated by comma: ")))
    finalscores = list(scores)
    print(sum(finalscores)/len(finalscores))
    
main()