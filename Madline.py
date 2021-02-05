yi = 0.0
dif = 0.0
w11 = 0.05
w12 = 0.1
w21 = 0.2
w22 = 0.2
b1 = 0.3
b2 = 0.15
V1 = V2 = B3 =0.5
Inputs=[[1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]]
Outputs =[-1, 1, 1, -1 ]
alpha = 0.5
for i in range(0, 15):
    print("Epoch", i + 1)
    print("X1\tX2\t\tT\t\tZin1\tZin2\tZ1\tZ2\tYin\t\tYi\t\tW11\t\tW21\t\tB1\t\tW12\t\tW22\t\tB2")
    print("============================================================================================================")
    for j in range(0,4):
        Zin1 = b1 + (Inputs[j][0]*w11)+(Inputs[j][1]*w21)
        Zin2 = b2 + (Inputs[j][0]*w12)+(Inputs[j][1]*w22)
        if Zin1 > 0:
            Z1 = 1
        else:
            Z1 = -1
        if Zin2 > 0:
            Z2 = 1
        else:
            Z2 = -1
        yi = B3 + (Z1*V1) +(Z2*V2)
        if yi > 0:
            y = 1
        else:
            y = -1
        if y == Outputs[j]:
            w11_new = 0
            w22_new = 0
            w21_new = 0
            w12_new = 0
        elif y !=Outputs[j] and Outputs[j] == 1:
            w11 = w11 + (alpha *(1-Zin1)*(Inputs[j][0]))
            w21 = w21 + (alpha *(1-Zin1)*Inputs[j][1])
            b1 = b1 + (alpha * (1 - Zin1))
            w12 = w12 + (alpha * (1 - Zin2) * Inputs[j][0])
            w22 = w22 + (alpha * (1 - Zin2) * Inputs[j][1])
            b2 = b2 + (alpha *(1-Zin2))
        elif y !=Outputs[j] and Outputs[j] == -1:
            w11 = w11 + (alpha *(-1-Zin1)*(Inputs[j][0]))
            w21 = w21 + (alpha *(-1-Zin1)*Inputs[j][1])
            b1 = b1 + (alpha * (-1 - Zin1))
            w12 = w12 + (alpha * (-1 - Zin2) * Inputs[j][0])
            w22 = w22 + (alpha * (-1 - Zin2) * Inputs[j][1])
            b2 = b2 + (alpha *(-1-Zin2))

        print(Inputs[j][0],"\t",Inputs[j][1],"\t",Outputs[j],"\t\t",round(Zin1,2),"\t",round(Zin2,2),"\t",Z1,"\t",Z2,"\t",yi,"\t",y,"\t",round(w11,3),"\t\t",round(w21,3),"\t\t",round(b1,3),"\t\t",round(w12,3),"\t\t",round(w22,3),"\t\t",round(b2,3),"\t\t")



