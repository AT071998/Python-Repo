def main():
    initial_w1  = 0
    initial_w2 = 0
    initial_b = 0
    alpha = 1
    for i in range(0,4):
        x1 = int(input("Enter the first Input:"))
        x2 = int(input("Enter the Second input:"))
        target = int(input("Enter the target"))
        y_in = initial_b + (x1*initial_w1)+(x2*initial_w2)
        if y_in > 1:
            y = 1
        else:
            y = -1
        if target != y:
            w11 = x1*target*alpha
            w22 = x2*target*alpha
            b1 = target*alpha
        else:
            w11 = 0
            w22 = 0
            b1 = 0
        initial_w1 = initial_w1 + w11
        initial_w2 = initial_w2 + w22
        initial_b = initial_b + b1
        print("x1\t\tx2\t\tt\t\tyin\t\ty\t\tw11\t\tw22\t\tb1\t\tw1\t\tw2\t\tb")
        print("==========================================================================================")
        print(x1,"\t\t",x2,"\t\t",target,"\t\t",y_in,"\t",y,"\t\t",w11,"\t\t",w22,"\t\t",b1,"\t\t",initial_w1,"\t\t",initial_w2,"\t\t",initial_b,"\t\t")


main()