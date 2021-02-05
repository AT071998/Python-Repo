
def main():
    V = [[0.6, 0.4],
         [0.6, 0.4],
         [0.4, 0.6],
         [0.4, 0.6]]
    W = [[0.3, 0.3],
         [0.3, 0.3]]
    alpha = 0.2
    beta = 0.2
    X = [1, 0, 1, 0]
    Y = [1, 0]
    print("V = ", V)
    print("W = ", W)
    print("X = ", X)
    print("Y = ", Y)
    print("======================================")
    J = Calculate(X, Y, V, W)
    print("J = ", J)
    print("Updated V is, V = ")
    V_New = V_Updation( J,V,  alpha, X,beta,Y)
    display_Matrix(V_New)
    print("======================================")
    print("Phase 2 Training")
    print('======================================')
    alpha = alpha/2
    beta = beta / 2
    print("Alpha = ",alpha)
    print("Beta = ",beta)
    J1 = Calculate(X, Y, V, W)
    print("J = ", J1)
    print("Updated V is, V = ")
    V_New1 = V_Updation( J1, V_New, alpha, X, beta, Y)
    display_Matrix(V_New1)
    print("=========================================")
    print("Transposing the matrix")
    print(" V = ")
    a = tranpose(V_New1)
    display_Matrix(a)
    print(" W = ")
    b = tranpose_Weight(W)
    display_Matrix(b)
    print("===========================")
    print("Updated V is V= ")
    V_New2 = V_UpdationT(J1, a, alpha, X, beta, Y)
    display_Matrix(V_New2)
    print("Updated W is, W = ")
    W_New2 = Weight_UpdationT(b, beta, Y, J1)
    display_Matrix(W_New2)





def Calculate(X, Y, V, W):
    D1 = round((((X[0] - V[0][0]) ** 2) + (X[1] - V[1][0]) ** 2 + + (X[2] - V[2][0]) ** 2 +  (X[3] - V[3][0]) ** 2 ),3)
    print("D1 = ",D1)
    D2 = round((((X[0] - V[0][1]) ** 2) + (X[1] - V[1][1]) ** 2 + + (X[2] - V[2][1]) ** 2 + (X[3] - V[3][1]) ** 2 ),3)
    print("D2 = ",D2)
    if D1 < D2:
        J = 1
    elif D2 < D1:
        J = 2
    elif D1 == D2:
        J = 1
    return J

def V_UpdationT(J,V,alpha,X,beta,Y):
    for i in range(0,4):
        if J == 1:
           V[0][i] = round(V[0][i] + (alpha*(X[i]-V[0][i])),3)
        else:
           V[1][i] = round(V[1][i] + (alpha *(X[i]-V[1][i])),3)
    return V

def V_Updation(J,V,alpha,X,beta,Y):
    for i in range(0,4):
        if J == 1:
           V[i][0] = round(V[i][0] + (alpha*(X[i]-V[i][0])),3)
        else:
           V[i][1] = round(V[i][1] + (alpha *(X[i]-V[i][1])),3)

    return V



def Weight_UpdationT(W,beta,Y,J):
    for i in range(0,2):
        if J == 1:
           W[0][i] = round(W[0][i] + (beta*(Y[i]-W[0][i])),3)
        else:
           W[1][i] = round(W[1][i] + (beta *(Y[i]-W[1][i])),3)
    return  W


def display_Matrix(matrix):
    for r in matrix:
        print(r)

def tranpose(matrix):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(matrix)):
        # iterate through columns
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

def tranpose_Weight(matrix):
    result = [[0, 0],
              [0, 0]]
    for i in range(len(matrix)):
        # iterate through columns
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result
main()