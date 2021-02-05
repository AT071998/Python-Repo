def main():
    S1 = [[1, 1, -1, -1]]
    S2 = [[1, -1, -1, -1]]
    S3 = [[1, 1, 1, 1]]
    S4 = [[-1, -1, -1, -1]]
    S1t = [[1], [1], [-1], [-1]]
    s2t = [[1], [-1], [-1], [-1]]
    s3t = [[1], [1], [1], [1]]
    s4t = [[-1], [-1], [-1], [-1]]
    print("S1=",S1)
    print("S2=",S2)
    print("S3=",S3)
    print("S4=",S4)
    print("W1")
    W1 = multiply(S1t,S1)
    display_matrix(W1)
    print("W2")
    W2 = multiply(s2t,S2)
    display_matrix(W2)
    print("W3")
    W3 = multiply(s3t, S3)
    display_matrix(W3)
    print("W4")
    W4 = multiply(s4t, S4)
    display_matrix(W4)
    print("===================")
    print("W")
    W_mid = add(W1,W2)
    W_mid2 = add(W4,W3)
    W = add(W_mid,W_mid2)
    display_matrix(W)
    print("Testing")
    print("Case 1")
    case1 = multiply_case(S1,W)
    print("Yin")
    display_matrix(case1)
    print("Y")
    a = calculate_Y(case1)
    print(a)
    print("=============")
    print("Case 2")
    case2 = multiply_case(S2, W)
    print("Yin")
    display_matrix(case2)
    print("Y")
    b = calculate_Y(case2)
    print(b)
    print("=============")
    print("Case 3")
    case3 = multiply_case(S3, W)
    print("Yin")
    display_matrix(case3)
    print("Y")
    c = calculate_Y(case3)
    print(c)
    print("=============")
    print("Case 4")
    case4 = multiply_case(S4, W)
    print("Yin")
    display_matrix(case4)
    print("Y")
    d = calculate_Y(case4)
    print(d)
    print("======================")
    print("Energy Calculation")
    E1= calculate_Energy(case1,S1t)
    print("E1=",E1)
    E2 = calculate_Energy(case2,s2t)
    print("E2=",E2)
    E3 = calculate_Energy(case3,s3t)
    print("E3=",E3)
    E4 = calculate_Energy(case4,s4t)
    print("E4=",E4)




def calculate_Y(matrix):
    result = [[0, 0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= 0:
                result[i][j] = -1
            else:
                result[i][j] = 1
    return result

def calculate_Energy(SW,Transpose):
    Ans = multiply_SW(SW,Transpose)
    for i in range(len(Ans)):
        for j in range(len(Ans[0])):
            Ans[i][j] = Ans[i][j] * (-1/2)
    return Ans

def add(matrix1, matrix2):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result




def display_matrix(matrix):
    for r in matrix:
        print(r)


def multiply(matrix,transpose):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                if i == j:
                    result[i][j] = 0
                else:
                    result[i][j] += matrix[i][k] * transpose[k][j]
    return result


def multiply_case(matrix,transpose):
    result = [[0, 0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                    result[i][j] += matrix[i][k] * transpose[k][j]
    return result

def multiply_SW(matrix,transpose):
    result = [[0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                    result[i][j] += matrix[i][k] * transpose[k][j]
    return result


main()

