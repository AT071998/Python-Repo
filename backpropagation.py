import math
def main():
    V = [[2, 1, 0],
         [1, 2, 2],
         [0, 3, 1]]
    Vo = [[0, 0, -1]]
    W = [[-1, 1, 2]]
    Wo = [[-1]]

    V11 = 2
    V21 = 1
    V31 = 0
    V12 = 1
    V22 = 2
    V32 = 3
    Vo2 = 0
    Vo1 = 0
    V13 = 0
    V23 = 2
    V33 = 1
    Vo3 = -1
    x1 = 0.6
    x2 = 0.8
    x3 = 0
    Wo1 =-1
    W11 = -1
    W21 = 1
    W31 = 2
    target = 0.9
    alpha = 0.3
    print("V =",V)
    print("Vo =",Vo)
    print("W =",W)
    print("Wo =",Wo)
    print("===========================")
    print("Calculating Zin1,Zin2,Zin3")
    print("========================")
    Zin1 = Vo1 + (x1*V11) + (x2*V21) + (x3*V31)
    print("Zin1 = ",Zin1)
    Zin2 = Vo2 + (x1*V12) + (x2*V22) + (x3*V32)
    print("Zin2 = ", Zin2)
    Zin3 = Vo3 + (x1 * V13) + (x2 * V23) + (x3 * V33)
    print("Zin3 = ", round(Zin3,1))
    print("===========================")
    Z1 = 1 / (1+math.exp(-Zin1) )
    print("Z1 =",round(Z1,5))
    Z2 = 1 / (1 + math.exp(-Zin2))
    print("Z2 =", round(Z2, 5))
    Z3 = 1 / (1 + math.exp(-Zin3))
    print("Z3 =", round(Z3, 5))
    print("===========================")
    Yink = Wo1+(Z1*W11)+(Z2*W21)+(Z3*W31)
    print("Yink=",round(Yink,4))
    y1 = 1 / (1+math.exp(-Yink))
    print("Y1=",round(y1,4))
    print("===========================")
    delK = (target-y1)*(y1)*(1-y1)
    print("DelK=",round(delK,4))
    delin1 = delK * W11
    print("Delin1 = ",round(delin1,4))
    delin2 = delK * W21
    print("Delin2 = ",round(delin2,4))
    delin3 = delK * W31
    print("Delin3 =",round(delin3,4))
    print("===========================")
    d1 = delin1 * Z1 * (1-Z1)
    print("D1 =",round(d1,4))
    d2 = delin2 * Z2 * (1 - Z2)
    print("D2 =", round(d2, 4))
    d3 = delin3 * Z3 * (1 - Z3)
    print("D3 =", round(d3, 4))
    print("===========================")
    print("Weight Updation")
    v11_new = V11 + (alpha*d1*x1)
    print("V11(New) = ",round(v11_new,4))
    v12_new = V12 + (alpha * d2 * x1)
    print("V12(New) = ", round(v12_new, 4))
    v13_new = V13 + (alpha * d3 * x1)
    print("V13(New) = ", round(v13_new, 4))
    v21_new = V21 + (alpha * d1 * x2)
    print("V21(New) = ", round(v21_new, 4))
    v22_new = V22 + (alpha * d2 * x2)
    print("V13(New) = ", round(v22_new, 4))
    v23_new = V23 + (alpha * d3 * x2)
    print("V12(New) = ", round(v23_new, 4))
    v31_new = V31 + (alpha * d1 * x3)
    print("V31(New) = ", round(v31_new, 4))
    v32_new = V32 + (alpha * d2 * x3)
    print("V32(New) = ", round(v32_new, 4))
    v33_new = V33 + (alpha * d3 * x3)
    print("V33(New) = ", round(v33_new, 4))
    Vo1_new = Vo1 + (alpha * d1)
    print("Vo1(New) = ", round(Vo1_new, 4))
    Vo2_new = Vo2 + (alpha * d2)
    print("Vo2(New) = ", round(Vo2_new, 4))
    Vo3_new = Vo3 + (alpha * d3)
    print("Vo1(New) = ", round(Vo3_new, 4))
    w11_new = W11 + (alpha * delK * Z1)
    print("w11(New) = ", round(w11_new, 4))
    w21_new = W21 + (alpha * delK * Z2)
    print("w21(New) = ", round(w21_new, 4))
    w31_new = W31 + (alpha * delK * Z3)
    print("w31(New) = ", round(w31_new, 4))
    Wo_new = Wo1 + (alpha*delK)
    print("Wo(New)= ",round(Wo_new,4))
    print("===========================")



main()