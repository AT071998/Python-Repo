def main():

    activations = [0.3,0.5, 0.7, 0.9]
    Weight = 0.2
    print("Initial values of activations are:", activations)
    print("Inhibitory Weight is:", Weight)
    print("=======================================")
    activation_old = activations.copy()
    activations_new = []
    count = 1
    while True:
        temp = sum(map(float, activation_old))
        print("Epoch{0}".format(count))
        for i in range(0, 4):
            value = activation_old[i] - Weight * temp + Weight * activation_old[i]
            print("A{0}{1}  =   {2} ".format(i, count, round(value,4)))
            if value > 0:
                activations_new.append(round(value,4))
            else:
                activations_new.append(0)
        activation_old = activations_new.copy()
        count += 1
        if sum(activations_new) == max(activations_new):
            break
        print("Activations obtained = {}".format( activation_old))
        print("================================================")
        activations_new = []

    print("Activations obtained = {}".format( activations_new))
    print("========================================================")

    i = 0
    while activations_new[i] == 0:
        i = i + 1
    print("Convergence has Occurred")

main()