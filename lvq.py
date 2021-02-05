def main():


    v1 = [1, 0, 1, 0, 1]
    v2 = [0, 0, 1, 1, 2]
    v3 = [1, 1, 0, 1, 2]
    v4 = [1, 1, 0, 0, 1]
    v5 = [0, 1, 1, 0, 2]
    alpha = 0.1

    print("V1:   ",v1)
    print("V2:   ",v2)
    print("V3:   ",v3)
    print("V4:   ",v4)
    print("V5:   ",v5)
    print("Alpha : ", alpha)
    c = 0

    print("EPOCH 1")

    w1 = v1
    w2 = v2
    x = v3
    print("X : ",x)
    d1 = round(((w1[0] - x[0])**2 + (w1[1] - x[1])**2 + (w1[2] - x[2])**2 + (w1[3] - x[3])**2), 4)
    d2 = round(((w2[0] - x[0])**2 + (w2[1] - x[1])**2 + (w2[2] - x[2])**2 + (w2[3] - x[3])**2), 4)
    print("D(1) :", d1)
    print("D(2) :", d2)
    if d1 < d2:
        c = w1[4]
    else:
        c = w2[4]
    print("C :", c)
    wNew = [0, 0, 0, 0, 0]
    for i in range(4):
        wNew[i] = x[i] - w1[i]
    for i in range(4):
        wNew[i] = round(wNew[i] * alpha, 4)
    for i in range(4):
        wNew[i] -= w1[i]
    wNew[4] = w1[4]
    print("W_New :",wNew)
    print("======================")
    x = v4
    print("X : ", x)

    d1 = round(((wNew[0] - x[0])**2 + (wNew[1] - x[1])**2 +(wNew[2] - x[2])**2 + (wNew[3] - x[3])**2), 4)
    d2 = round(((w2[0] - x[0])**2 + (w2[1] - x[1])**2 +(w2[2] - x[2])**2 + (w2[3] - x[3])**2), 4)
    print("D(1) :", d1)
    print("D(2) :", d2)
    if d1 < d2:
        c = wNew[4]
    else:
        c = w2[4]
    print("C :", c)

    wNew2 = [0, 0, 0, 0, 0]

    for i in range(4):
        wNew2[i] = x[i] - wNew[i]
    for i in range(4):
        wNew2[i] = round(wNew[i] * alpha, 4)
    for i in range(4):
        wNew2[i] -= w1[i]
    wNew2[4] = w2[4]

    print("W_New :", wNew2)
    print("==============================")
    x = v5
    print("X : ", x)
    d1 = round(((wNew[0] - x[0])**2 + (wNew[1] - x[1])**2 +(wNew[2] - x[2])**2 + (wNew[3] - x[3])**2), 4)
    d2 = round(((wNew2[0] - x[0])**2 + (wNew2[1] - x[1])**2 +(wNew2[2] - x[2])**2 + (wNew2[3] - x[3])**2), 4)
    print("D(1) :", d1)
    print("D(2) :", d2)
    if d1 < d2:
        c = wNew[4]
    else:
        c = wNew2[4]
    print("C :", c)

    wNew3 = [0, 0, 0, 0, 0]

    for i in range(4):
        wNew3[i] = x[i] - wNew2[i]
    for i in range(4):
        wNew3[i] = round(wNew3[i] * alpha, 4)
    for i in range(4):
        wNew3[i] = round(wNew3[i] - wNew[i], 4)
    wNew3[4] = wNew2[4]

    print("W_New :", wNew3)
    print("==========================")
    print("Reducing the Learning rate ")
    alpha = 0.5 * alpha
    print("Alpha :", alpha)

    print("EPOCH - 2")

    w1 = wNew3
    x = v3
    print("X : ",x)
    d1 = round(((w1[0] - x[0])**2 + (w1[1] - x[1])**2 +(w1[2] - x[2])**2 + (w1[3] - x[3])**2),3)
    d2 = round(((w2[0] - x[0])**2 + (w2[1] - x[1])**2 +(w2[2] - x[2])**2 + (w2[3] - x[3])**2),3)

    print("D(1) :", d1)
    print("D(2) :", d2)

    if d1 < d2:
        c = w1[4]
    else:
        c = w2[4]

    print("C :", c)

    wNew = [0, 0, 0, 0, 0]

    for i in range(4):
        wNew[i] = x[i] - w1[i]
    for i in range(4):
        wNew[i] = round(wNew[i] * alpha, 4)
    for i in range(4):
        wNew[i] = round(wNew[i] + w1[i], 4)
    wNew[4] = w1[4]

    print("W_New :",wNew)
    print("=========================================")
    x = v4
    print("X : ", x)
    d1 = round(((wNew[0] - x[0])**2 + (wNew[1] - x[1])**2 +(wNew[2] - x[2])**2 + (wNew[3] - x[3])**2),3)
    d2 = round(((w2[0] - x[0])**2 + (w2[1] - x[1])**2 +(w2[2] - x[2])**2 + (w2[3] - x[3])**2),3)
    print("D(1) :", d1)
    print("D(2) :", d2)
    if d1 < d2:
        c = wNew[4]
    else:
        c = w2[4]
    print("C :", c)

    wNew2 = [0, 0, 0, 0, 0]

    for i in range(4):
        wNew2[i] = x[i] - wNew[i]
    for i in range(4):
        wNew2[i] = round(wNew[i] * alpha, 4)
    for i in range(4):
        wNew2[i] = round(wNew2[i] + w1[i], 4)
    wNew2[4] = w2[4]

    print("W_New :",wNew2)
    print("================================")
    x = v5
    print("X : ", x)
    d1 = round(((wNew[0] - x[0])**2 + (wNew[1] - x[1])**2 +(wNew[2] - x[2])**2 + (wNew[3] - x[3])**2), 3)
    d2 = round(((w2[0] - x[0])**2 + (w2[1] - x[1])**2 +(w2[2] - x[2])**2 + (w2[3] - x[3])**2), 3)
    print("D(1) :", d1)
    print("D(2) :", d2)

    if d1 < d2:
        c = wNew[4]
    else:
        c = wNew2[4]
    print("C :", c)

    wNew3 = [0, 0, 0, 0, 0]

    for i in range(4):
        wNew3[i] = x[i] - wNew2[i]
    for i in range(4):
        wNew3[i] = round(wNew3[i] * alpha, 4)
    for i in range(4):
        wNew3[i] = round(wNew3[i] + wNew[i], 4)
    wNew3[4] = wNew2[4]

    print("W_New :",wNew3)
    print("Hence learning rate is ",alpha)
    print("Thus LVQ net is constructed and tested")

main()