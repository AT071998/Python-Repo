def main():
   X1 = [[1, 0, 1]]
   X1t= [[1], [0], [1]]
   X2t =[[0], [1], [0]]
   X2 = [[0, 1, 0]]
   Y1 = [[1, 0]]
   Y2 = [[0, 1]]
   print("X1=", X1)
   print("X2=", X2)
   print("Y1=", Y1)
   print("Y2=", Y2)
   print("W1")
   W1 = multiply(X1t,Y1)
   display_matrix(W1)
   print("W2")
   W2 = multiply(X2t, Y2)
   display_matrix(W2)
   print("W")
   W = add(W1,W2)
   display_matrix(W)
   print("=============================")
   print("Testing:X-->Y")
   print("Case 1")
   case1 = test(X1,W)
   print("Yin")
   display_matrix(case1)
   print("Y")
   a = calculate_final(case1)
   display_matrix(a)
   check_result(a,Y1)
   print("=============================")
   print("Case 2")
   case2 = test(X2, W)
   print("Yin")
   display_matrix(case2)
   print("Y")
   b=calculate_final(case2)
   display_matrix(b)
   check_result(b,Y2)
   print("=============================")
   print("Testing:Y-->X")
   print("Transpose W:")
   WT = tranpose(W)
   display_matrix(WT)
   print("=============================")
   print("Case 3")
   case3 = test2(Y1, WT)
   print("Yin")
   display_matrix(case3)
   print("Y")
   c = calculate_final2(case3)
   display_matrix(c)
   check_result(c, X1)
   print("=============================")
   print("Case 4")
   case4 = test2(Y2, WT)
   print("Yin")
   display_matrix(case4)
   print("Y")
   d = calculate_final2(case4)
   display_matrix(d)
   check_result(d, X2)
   print("Bipolar")
   X3 =[[1,-1,1]]
   X3t =[[1],[-1],[1]]
   X4 = [[-1,1,-1]]
   X4t =[[-1],[1],[-1]]
   Y3=[[1,-1]]
   Y4=[[-1,1]]
   print("X1=", X3)
   print("X2=", X4)
   print("Y1=", Y3)
   print("Y2=", Y4)
   print("W1")
   W1 = multiply(X3t, Y3)
   display_matrix(W1)
   print("W2")
   W2 = multiply(X4t, Y4)
   display_matrix(W2)
   print("W")
   W = add(W1, W2)
   display_matrix(W)
   print("=============================")
   print("Testing:X-->Y")
   print("Case 1")
   case1 = test(X3, W)
   print("Yin")
   display_matrix(case1)
   print("Y")
   a = calculate_final3(case1)
   display_matrix(a)
   check_result(a, Y3)
   print("=============================")
   print("Case 2")
   case2 = test(X4, W)
   print("Yin")
   display_matrix(case2)
   print("Y")
   b = calculate_final3(case2)
   display_matrix(b)
   check_result(b, Y4)
   print("=============================")
   print("Testing:Y-->X")
   print("Transpose W:")
   WT = tranpose(W)
   display_matrix(WT)
   print("=============================")
   print("Case 3")
   case3 = test2(Y3, WT)
   print("Yin")
   display_matrix(case3)
   print("Y")
   c = calculate_final4(case3)
   display_matrix(c)
   check_result(c, X3)
   print("=============================")
   print("Case 4")
   case4 = test2(Y4, WT)
   print("Yin")
   display_matrix(case4)
   print("Y")
   d = calculate_final4(case4)
   display_matrix(d)
   check_result(d, X4)



def check_result(matrix,target):
    if matrix == target:
        print("Target matches")
    else:
        print("Target does not matches")


def calculate_final2(matrix):
    result = [[0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= 0:
                result[i][j] = 0
            else:
                result[i][j] = 1
    return result
def calculate_final4(matrix):
    result = [[0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= 0:
                result[i][j] = -1
            else:
                result[i][j] = 1
    return result

def calculate_final3(matrix):
    result = [[0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= 0:
                result[i][j] = -1
            else:
                result[i][j] = 1
    return result

def calculate_final(matrix):
    result = [[0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= 0:
                result[i][j] = 0
            else:
                result[i][j] = 1
    return result

def test(matrix,transpose):
    result = [[0, 0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                    result[i][j] += matrix[i][k] * transpose[k][j]
    return result


def test2(matrix,transpose):
    result = [[0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                    result[i][j] += matrix[i][k] * transpose[k][j]
    return result


def tranpose(matrix):
    result = [[0, 0, 0],
             [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


def multiply(matrix,transpose):
    result = [[0, 0],
              [0, 0],
              [0, 0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                    result[i][j] += matrix[i][k] * transpose[k][j]
    return result


def display_matrix(matrix):
    for r in matrix:
        print(r)


def add(matrix1, matrix2):
    result = [[0, 0],
              [0, 0],
              [0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

main()