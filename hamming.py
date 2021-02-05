

def main():
    E1 = [-1, 1, -1, 1]
    E2 = [1, -1, -1, -1]
    E = [[-1, 1],
         [1, -1],
         [-1, -1],
         [1, -1]]
    print("E1  = ",E1)
    print("E2  = ",E2)
    print("========================")
    print("E is a matrix i,e  ")
    display(E)
    print("=====================")
    print("Calculating Weight matrix")
    W = multiply_Scalar(E)
    print("W = ")
    display(W)
    b1 = b2 = len(E) / 2
    print("B1 = B2 = ",b1)
    print("=====================")
    print("Case 1: ")
    X = [1, 1, -1, -1]
    print("X=", X)
    calculate_Yin(X,b1,b2,W)
    print("====================")
    print("Case 2: ")
    X = [-1, 1, 1, -1]
    print("X= ",X)
    calculate_Yin(X,b1,b2,W)
    print("====================")
    print("Case 3: ")
    X = [-1, -1, -1, 1]
    print("X= ", X)
    calculate_Yin(X, b1, b2, W)
    print("====================")
    print("Case 4: ")
    X = [-1, -1, 1, 1]
    print("X= ", X)
    calculate_Yin(X, b1, b2, W)


def multiply_Scalar(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j] * (1/2)
    return matrix


def calculate_Yin(X, B1, B2, W):
    Yin1 = B1 + ((X[0]*W[0][0])+(X[1]*W[1][0])+(X[2]*W[2][0])+(X[3]*W[3][0]))
    print("Yin1  = ",Yin1)
    Yin2 = B2 + ((X[0]*W[0][1])+(X[1]*W[1][1])+(X[2]*W[2][1])+(X[3]*W[3][1]))
    print("Yin2 = ",Yin2)
    if Yin1 > Yin2:
        print("Y1 is the best exempler for the input Vector {0}".format(X))
    else:
        print("Y2 is the best exempler for the input Vector {0}".format(X) )


def display(matrix):
    for i in matrix:
        print(i)



main()