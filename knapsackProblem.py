# coding=utf-8

from simpleai.search import SearchProblem
from simpleai.search.local import *
import random

numberOfItems = int(input("Enter number of items: "))
knapsackCapacity = int(input("Enter knapsack capacity: "))
weight = []

for i in range(numberOfItems):
    print("Enter of %d. weight : " % (i + 1), end="")
    weight.append(int(input()))

value = []
for i in range(numberOfItems):
    print("Enter of %d. value : " % (i + 1), end="")
    value.append(int(input()))

bag = []
for i in range(numberOfItems):
    bag.append(0)

# print(len(bag))

print("# items: ", numberOfItems)
print("Capacity: ", knapsackCapacity)
print("Weights: ", weight)
print("Values: ", value)



def listToString(s):
    str1 = ""
    for i in range(len(s)):
        str1 += str(s[i])
    return str1


def stringToList(s):
    list1 = []
    for i in range(len(s)):
        list1.append(int(s[i]))
    return list1


class knapsackProblem(SearchProblem):
    def actions(self, state):
        return listToString(range(len(state)))

    def result(self, state, action):
        if (state[int(action)]) == '0':
            return state[:int(action)] + '1' + state[int(action) + 1:]

        else:
            return state[:int(action)] + '0' + state[int(action) + 1:]



    def value(self, state):
        totalWeight = 0
        for i in range(len(state)):
            totalWeight += int(state[i]) * weight[i]
        if (totalWeight > knapsackCapacity):
            return 0

        totalValue = 0
        for i in range(len(state)):
            totalValue += int(state[i]) * value[i]
        #print(totalValue)
        return totalValue

    def generate_random_state(self):

        temp = []
        for i in range(numberOfItems):
            temp.append(random.choice('01'))
        return listToString(temp)

    def crossover(self, state1, state2):
        cut_point = random.randint(0, numberOfItems)
        child = state1[:cut_point] + state2[cut_point:]
        return child

    def mutate(self, state):
        mutation = random.choice(' 01')
        mutation_point = random.randint(0, numberOfItems)
        mutated = ''.join([state[i] if i != mutation_point else mutation
                           for i in range(len(state))])
        return mutated


problem = knapsackProblem(initial_state=listToString(bag))

result = genetic(problem, population_size=numberOfItems, mutation_chance=0.1,
    iterations_limit=0, viewer=None)


#result = hill_climbing(problem, iterations_limit=0, viewer=None)


#restarts_limit = int(input("Enter a restarts limit: "))
#result = hill_climbing_random_restarts(problem, restarts_limit, iterations_limit=0, viewer=None)

totalWeight = 0
for i in range(len(result.state)):
    totalWeight += int(result.state[i]) * weight[i]
print("Total weight of the selected items: %d " %totalWeight)

totalValue = 0
for i in range(len(result.state)):
    totalValue += int(result.state[i]) * value[i]
print("Total profit of the selected items: %d" %totalValue)

print(result.state)
print("The list of items selected:", result.path())
