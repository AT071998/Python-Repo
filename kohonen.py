import math
""" Kohonen self organizing map is shown with the weights ,
 i) Using the square of Euclidian distance find the cluster unit Cj that is closest to the input vector (0.3, 0.4) 
   ii)  Using a learning rate of 0.3 find the new weights for the unit Cj   
   iii)  Find the new weights for Cj-1 and Cj+1, if they are allow to learn"""

class SOM:

    def winner(self, weights, sample):
        list_of = list()
        for i in range(0,5):
            D0 = 0
            D0 = math.pow((sample[0] - weights[0][i]), 2) +  math.pow((sample[1] - weights[1][i]), 2)
            print("D({0})=".format(i+1),round(D0,3))
            list_of.append(round(D0,3))
        print("Hence Obtained Eucledian Distances are:", list_of)
        minpos = list_of.index(min(list_of))
        return minpos

        # Function here updates the winning vector
    def update(self, weights, sample, J, alpha):
        print("==================================")
        print("Updating the Matrix at the Unit {0}".format(J+1))
        for i in range(0,len(weights)):
            weights[i][J]= round(weights[i][J] + alpha * (sample[i] - weights[i][J]),2)
            print("W{0}{1}=".format(i+1,J+1),round(weights[i][J],2))

        return weights

    # Driver code


def main():
    T = [[0.3, 0.4]]
    alpha = 0.3
    m, n = len(T), len(T[0])
    print("Kohonen Self Learning Feature Map")
    print("=============================================")
    weights = [[0.2, 0.6, 0.4, 0.9, 0.2],
               [0.3, 0.5, 0.7, 0.6, 0.8]]
    print("Initial Weights:")
    display_matrix(weights)
    print("X1= ",T[0][0])
    print("X2= ",T[0][1])
    print("Alpha= ",alpha)
    print("============================================")
    ob = SOM()
    epochs = 1

    for i in range(1):
        for j in range(m):
            sample = T[j]
            J = ob.winner(weights, sample)
            print("cluster unit Cj that is closest to the input vector (0.3, 0.4) is present at the position: ",J+1)
            weights = ob.update(weights, sample, J, alpha)
            print(weights)
            C1 = J - 1
            C2 = J + 1
            if C1 == 0 or C2 == 0:
                  pass

            if C2 !=0:
                weights = ob.update(weights, sample, C2, alpha)
            display_matrix(weights)

def display_matrix(mat):
    for r in mat:
        print(r)

if __name__ == "__main__":
    main()