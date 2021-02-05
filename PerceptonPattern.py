

def calculate():
    initial_w1  = 0
    initial_w2 = 0
    initial_w3 = 0
    initial_w4 = 0
    initial_b = 0
    alpha = 1
    check_list = []
    for i in range(0,2):
        x1 = int(input("Enter the first Input:"))
        x2 = int(input("Enter the Second input:"))
        x3 = int(input("Enter the third Input:"))
        x4 = int(input("Enter the fourth input:"))
        target = int(input("Enter the target:"))
        y_in = initial_b + (x1*initial_w1)+(x2*initial_w2) + (x3*initial_w3)+(x4*initial_w4)
        if y_in > 1:
            y = 1
        else:
            y = -1
        if target != y:
            w11 = x1*target*alpha
            w22 = x2*target*alpha
            w33 = x3*target*alpha
            w44 = x4*target*alpha
            b1 = target*alpha
        else:
            w11 = 0
            w22 = 0
            w33 = 0
            w44 = 0
            b1 = 0
        initial_w1 = initial_w1 + w11
        initial_w2 = initial_w2 + w22
        initial_w3 = initial_w3 + w33
        initial_w4 = initial_w4 + w44
        initial_b = initial_b + b1
        print("x1\t\tx2\t\tx3\t\tx4\t\tt\t\tyin\t\ty\t\tw11\t\tw22\t\tw33\t\tw44\t\tb1\t\tw1\t\tw2\t\tw3\t\tw4\t\tb")
        print("==========================================================================================================================================")
        print(x1,"\t\t",x2,"\t\t",x3,"\t\t",x4,"\t\t",target,"\t\t",y_in,"\t",y,"\t\t",w11,"\t\t",w22,"\t\t",w33,"\t\t",w44,"\t\t",b1,"\t\t",initial_w1,"\t\t",initial_w2,"\t\t",initial_w3,"\t\t",initial_w4,"\t\t",initial_b,"\t\t")
    check_list.append(initial_w1)
    check_list.append(initial_w2)
    check_list.append(initial_w3)
    check_list.append(initial_w4)
    check_list.append(initial_b)
    return check_list



def validate():
    for i in range(0,2):
        a = calculate()
        print("Pattern obtained for the class is",a)


validate()
