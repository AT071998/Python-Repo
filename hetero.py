def main():
    s1 = [[1, 1, 0, 0]]
    s2 = [[0, 1, 0, 0]]
    s3 = [[0, 0, 1, 1]]
    s4 = [[0, 0, 1, 0]]

    s1t = [[1], [1], [-1], [-1]]
    t1 = [[1, -1]]
    s2t = [[-1], [1], [-1], [-1]]
    t2 = [[1, -1]]
    s3t = [[-1], [-1], [1], [1]]
    t3 = [[-1, 1]]
    s4t = [[-1], [-1], [1], [-1]]
    t4 = [[-1, 1]]


    w1 = matrix_multiply(s1t, t1)
    w2 = matrix_multiply(s2t, t2)
    w3 = matrix_multiply(s3t, t3)
    w4 = matrix_multiply(s4t, t4)

    w = matrix_addition(w1, w2)
    w = matrix_addition(w, w3)
    w = matrix_addition(w, w4)

    print("S1")
    print_matrix(s1)
    print("S2")
    print_matrix(s2)
    print("S3")
    print_matrix(s3)
    print("S4")
    print_matrix(s4)
    print("==================")
    print("W1")
    print_matrix(w1)
    print("W2")
    print_matrix(w2)
    print("W3")
    print_matrix(w3)
    print("W4")
    print_matrix(w4)
    print("W")
    print_matrix(w)
    print("================")
    print("Case 1")
    print_matrix(calculate_final(calculate(s1, w)))
    check_match(calculate(s1, w), t1)
    print("Case 2")
    print_matrix(calculate_final(calculate(s2, w)))
    check_match(calculate(s2, w), t2)
    print("Case 3")
    print_matrix(calculate_final(calculate(s3, w)))
    check_match(calculate(s3, w), t3)
    print("Case 4")
    print_matrix(calculate_final(calculate(s4, w)))
    check_match(calculate(s4, w), t4)


def matrix_multiply(mat1, mat2):
    result = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def matrix_addition(mat1, mat2):
    result = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(len(mat1)):
        # iterate through columns
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result


def calculate(A, B):
    result = [[0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def calculate_final(mat2):
    result = [[0, 0]]
    for i in range(len(mat2)):
        for j in range(len(mat2[0])):
            if mat2[i][j] > 0:
                result[i][j] = 1
            else:
                result[i][j] = -1
    return result


def check_match(obtained, t):
    if calculate_final(obtained) == t:
        print("Obtained Value = T,Hence Equal")
    else:
        print("Not Equal")


def print_matrix(m):
    for i in m:
        print(i)

main()