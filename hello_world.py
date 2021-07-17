# coding=utf-8

from __future__ import print_function

from simpleai.search import SearchProblem, astar, breadth_first, depth_first, uniform_cost, greedy, limited_depth_first,iterative_limited_depth_first
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer
GOAL = 'AB'

my_viewer = WebViewer()
class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' AB')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
#BFS
result = breadth_first(problem, viewer=my_viewer)
print("BFS: ")
print(result.state)
print(result.path())

print('Stats: ')
print(my_viewer.stats)
