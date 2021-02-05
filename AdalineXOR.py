yi = 0.0
dif = 0.0
w1 = 0.2
w2 = 0.2
b = 0.2
Inputs=[[1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]]
Outputs =[-1, 1, -1, -1 ]
alpha = 0.2
for i in range(0, 6):
    print("Epoch", i + 1)
    print("X1\t\tX2\t\tT\t\t\tYin\t\t\t(T-Yin)\t\t\tdw1\t\t\tdw2\t\t\tdb\t\t\tw1\t\t\tw2\t\t\tb\t\t\t(T-Yin)Square")
    print("=======================================================================================================================================")
    errors = []
    avg = 0.0
    for j in range(0 ,4):
        yi = Inputs[j][0] * w1 + Inputs[j][1] * w2 + 1 * b
        dif = Outputs[j] - yi
        dw1 = 0.2 * dif * Inputs[j][0]
        dw2 = 0.2 * dif * Inputs[j][1]
        db = 0.2 * dif * 1
        w1 += dw1
        w2 += dw2
        b += db
        err = dif * dif
        errors.append(err)
        print(Inputs[j][0],"\t\t",Inputs[j][1],"\t\t",Outputs[j],"\t\t",round(yi,3),"\t\t",round(dif,3),"\t\t",round(dw1,3),"\t\t",round(dw2,3),"\t\t",round(db,3),"\t\t",round(w1,3),"\t\t",round(w2,3),"\t\t",round(b,3),"\t\t",round(errors[j],3))
        avg += errors[j]
    print("Total Mean Square", round(avg,3))
print("Training is Completed")




