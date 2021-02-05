
yi = 0.0
dif = 0.0
w1 = 0.2
w2 = 0.1
w3 = 0.15
w4 = 0.25
b = 0.2
Inputs=[[1, 1,-1,-1],
        [-1,1,1,-1],
        [1,-1,-1,1],
        [-1,-1,1,1]]
Outputs =[1, -1, 1, -1 ]
alpha = 0.2
for i in range(0, 3):
    print("Epoch", i + 1)
    print("X1\tX2\tX3\tX4\tT\tYin\t(T-Yin)\tdw1\tdw2\tdw3\tdw4\tdb\tw1\tw2\tw3\tw4\tb\t(T-Yin)Square\t")
    print("===================================================================================")
    errors = []
    avg = 0.0
    for j in range(0 ,4):
        yi = Inputs[j][0] * w1 + Inputs[j][1] * w2 + Inputs[j][2]* w3 + Inputs[j][3]*w4 + 1 * b
        dif = Outputs[j] - yi
        dw1 = 0.2 * dif * Inputs[j][0]
        dw2 = 0.2 * dif * Inputs[j][1]
        dw3 = 0.2 * dif * Inputs[j][2]
        dw4 = 0.2 * dif * Inputs[j][3]
        db = 0.2 * dif * 1
        w1 += dw1
        w2 += dw2
        w3 += dw3
        w4 += dw4
        b += db
        err = dif * dif
        errors.append(err)
        print(Inputs[j][0],"\t",Inputs[j][1],"\t",Inputs[j][2],"\t",Inputs[j][3],"\t",Outputs[j],"\t",round(yi,3),"\t",round(dif,3),"\t",round(dw1,3),"\t",round(dw2,3),"\t",round(dw3,3),"\t",round(dw4,3),"\t",round(db,3),"\t",round(w1,3),"\t",round(w2,3),"\t",round(w3,3),'\t',round(w4,3),"\t",round(b,3),"\t",round(errors[j],2))
        avg += errors[j]
        if j == 2:
            yi = 0.0
            dif = 0.0
            w1 = 0.2
            w2 = 0.1
            w3 = 0.15
            w4 = 0.25
            b = 0.2
            dw1, dw2, dw3, dw4, db = 0 , 0 , 0 , 0 , 0
    print("Total Mean Square", round(avg,3))
print("Training is Completed")




