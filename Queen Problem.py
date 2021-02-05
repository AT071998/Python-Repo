import random as r
import numpy as np
qsize = 8

populations_size = 200
max_iteration = 50
best_solution = []
population_list= []

new_population = []
for i in range(populations_size):
    sel_pop = np.arange(qsize)
    np.random.shuffle(sel_pop)
    population_list.append(sel_pop.tolist())

#print(len(population_list))

def find_clashes(a):
    global best_solution
    clash_no = 0
    rcclash = a
    clash_no += len(rcclash) - len(np.unique(rcclash))
    for i1 in range(len(rcclash)):
        for j1 in range(len(rcclash)):
            if (i1 != j1):
                indexval = abs(i1 - j1)
                valpop = abs(rcclash[i1] - rcclash[j1])
                if (indexval == valpop):
                    clash_no += 1
    clash = 28 - clash_no

    #opt_sol = []

    print(rcclash, clash, clash_no)
    numofiter = 0
    if (clash == 28):

        # opt_sol.append(rcclash[i])
        print("\n-----------------------------------------------------------------------------\n")
        print("\nOptimal solution\n")
        print(rcclash)
        best_solution.append(rcclash)
        print("\n--------------------------------------------------------------------------\n")
        numofiter+=1
    #return (best_solution)




def recombine():
    global population_list
    global new_population

    for iter in range(max_iteration):
        print(iter)
        if(iter >= 1 ):
            population_list = new_population
            new_population = []

        #new_population = []
        lists = []
        cr1 = []
        cr2 = []
        for j in range(populations_size):
            a1 = r.randint(0, populations_size - 1)
            if (a1 not in cr1):
                cr1.append(a1)
            if (len(cr1) == round(populations_size / 2)):
                break

        for j in range(populations_size):
            if (j not in cr1):
                cr2.append(j)

        for j in range(round(populations_size / 2)):
            a1 = r.randint(0, qsize - 1)
            while(a1==0):
                a1 = r.randint(0, qsize - 1)
            lists.append(a1)

        print(cr1)
        print(cr2)
        print(lists)
        for i in range(round(populations_size / 2)):
            p1 = cr1[i]
            p2 = cr2[i]
            cross_over_point = lists[i]
            parent_1 = population_list[p1]
            parent_2 = population_list[p2]

            p3 = parent_2[0:cross_over_point]
            p11 = parent_1[0:cross_over_point]
            p4 = parent_2[cross_over_point:]
            p12 = parent_1[cross_over_point:]
            p3.extend(p12)
            p11.extend(p4)

            new_population.append(p3)
            new_population.append(p11)
        print("\n-------------------------------------------\n")
        for k in range(len(new_population)):
            find_clashes(new_population[k])
            mp1 = r.randint(0, qsize - 1)
            mp2 = r.randint(0, qsize - 1)
            while(mp1 == mp2):
                mp1 = r.randint(0, qsize - 1)
                mp2 = r.randint(0, qsize - 1)
            if (mp1 != mp2):
                #print(mp1,mp2)
                new_population[k][mp1], new_population[k][mp2] = new_population[k][mp2], new_population[k][mp1]

for i in range(len(population_list)):
    find_clashes(population_list[i])

recombine()
if(len(best_solution)==0):
    print("No solution")
else:
    print("Best Solution ",best_solution)
