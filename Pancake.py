# coding=utf-8

from __future__ import print_function
from simpleai.search import SearchProblem, astar, breadth_first, depth_first, uniform_cost, greedy, limited_depth_first, iterative_limited_depth_first
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer
import random

N = int(input("Enter number of pancakes: "))
order = input("Do you want to enter ordering?: YES/NO ")
my_list = []

if(order=="yes"):
    my_list = list(map(int, input("Enter the top to bottom ordering between [0-N], separeted bu spaces : ").strip().split()))[:N]
else:
    for i in range(N):
        my_list.append(i)
    random.shuffle(my_list)

print("initial state: (",end="")
print(*my_list,sep=",",end="")
print(")")

cost = 0
def spatula(inp_liste, spatula):
    global cost
    cost = spatula + 1
    a = int((spatula/2)+1)
    for i in range(a):
        temp = inp_liste[i]
        inp_liste[i]=inp_liste[spatula-i]
        inp_liste[spatula-i]=temp
    return inp_liste


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

def unsorted(state):
    for i in range (len(state)):
        j=len(state) - 1 - i
        if(state[j]!=GOAL[j]):
            return int(GOAL[j]) + 1
    return 0

GOAL = listToString(sorted(my_list))
my_viewer = WebViewer()


class PancakeProblem(SearchProblem):
    def actions(self, state):
        if not (state == GOAL):
            return listToString(range(1,unsorted(state)))
        else:
            return []

    def result(self, state, action):
        return listToString( spatula(stringToList(state), int(action)))

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        #return heuristic1(self, state)  # Our first heuristic funciton
        return heuristic2(self, state) #second heuristic function

    def cost(self, state, action, state2):
        return cost


def heuristic1(self, state):
    for i in range(len(state)):
        j = len(state) - 1 - i
        if (state[j] != GOAL[j]):
            reward = 0.5 if GOAL[j] == state[0] else 0
            return int(GOAL[j]) + 1 - reward
    return 0


def heuristic2(self, state):
    groups = 1
    reward = 1 if GOAL[len(state) - 1] == state[len(state) - 1] else 0
    for i in range(len(state) - 1):
        diff = int(state[i]) - int(state[i + 1])
        if abs(diff) != 1:
            groups += 1
    return groups - reward


'''
#v2
    def heuristic(self, state):
        groups = 1
        reward = 1 if GOAL[len(state)-1] == state[len(state)-1] else 0
        for i in range(len(state) - 1):
            diff = int(state[i]) - int(state[i + 1])
            if abs(diff) != 1:
                groups += 1
        return groups - reward



#v1.3 Our first heuristic func
    def heuristic(self, state):
        global unsorted
        for i in range(len(state)):
            j = len(state) - 1 - i
            if (state[j] != GOAL[j]):
                reward = 0.5 if GOAL[j] == state[0] else 0
                unsorted = int(GOAL[j]) + 1
                return int(GOAL[j]) + 1 - reward
        return 0

#v1.1
     def heuristic(self, state):
         global unsorted
         for i in range(len(state)):
             j = len(state) - 1 - i
             if(state[j] != GOAL[j]):
                 unsorted = int(GOAL[j]) + 1
                 return int(GOAL[j]) + 1
         return 0

#v1.0
    def heuristic(self, state):
        for i in range(len(state)):
             j=len(state) - 1 - i
             if(state[j] != GOAL[j]):
                return int(GOAL[j]) + 1 
        return 0
'''

problem = PancakeProblem(initial_state=listToString(my_list))

# BFS
#result = breadth_first(problem, viewer=my_viewer)
#print("BFS: ")

# DFS
# result = depth_first(problem, viewer=my_viewer)
# print("DFS: ")

# UCS
# result = uniform_cost(problem, viewer=my_viewer)
# print("UCS: ")

# Greedy S
result = greedy(problem, viewer=my_viewer)
print("GREEDY S: ")

# DLS
# result = limited_depth_first(problem, (N-1)*2-1 , viewer=my_viewer)
# print(" DLS: ")

# iterative DLS
# result = iterative_limited_depth_first(problem, viewer=my_viewer)
# print("iterative DLS: ")

# A*
# result = astar(problem, viewer=my_viewer)
# print("A*:")


print(result.state)
print(result.path())

print('Stats: ')
print(my_viewer.stats)
