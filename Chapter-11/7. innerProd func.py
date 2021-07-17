def innerProd(x, y):
    newSeq = []
    for i in range(len(x)):
        newSeq.append(x[i] * y[i])
    return sum(newSeq)

if __name__ == '__main__':
    '''Testing Function'''
    mySeq1 = [1,8,9,8]
    mySeq2 = [3,6,7,4]
    print(innerProd(mySeq1, mySeq2))