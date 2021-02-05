def main():
    s1 = [[1, 1, -1, -1]]
    s2 = [[-1, 1, 1, -1]]
    s3 = [[-1, 1, -1, 1]]

    store_vector = [[1, 1, 1, 1]]
    s1t = [[1], [1], [-1], [-1]]
    s2t = [[-1], [1], [1], [-1]]
    s3t = [[-1], [1], [-1], [1]]
    s4t = [[1], [1], [1], [1]]
    print("S1=", s1)
    print("S2=", s2)
    print("S3=", s3)
    print("W1")
    W1 = multiply(s1t,s1)
    display_matrix(W1)
    print("W2")
    W2 = multiply(s2t,s2)
    display_matrix(W2)
    print("W3")
    W3 = multiply(s3t,s3)
    display_matrix(W3)
    print("W")
    w_1 = add(W1 , W2)
    w_2 = add(w_1, W3)
    display_matrix(w_2)
    print("========================")
    print("Vector to be stored:",store_vector)
    print("W4")
    W4 = multiply(s4t, store_vector)
    display_matrix(W4)
    print("W_new = W_old + W4")
    W_New = add(w_2, W4)
    display_matrix(W_New)
    check_result(W_New)



def multiply(matrix,transpose):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(transpose[0])):
            for k in range(len(transpose)):
                result[i][j] += matrix[i][k] * transpose[k][j]
    return result


def add(matrix1, matrix2):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if j == i:
                result[i][j] = 0
            else:
                result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result


def check_result(matrix):
    if matrix == [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]:
        print("Pattern can be stored Successfully!!")
    else:
        pass

def display_matrix(matrix):
    for r in matrix:
        print(r)


main()