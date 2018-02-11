'''
Created on Feb 6, 2018

This is the depth-first search algorithm

The inputs are the initial state and the goal state, represented as arrays

The output are the nodes added to and popped from the frontier 

@author: dabrown
'''



import numpy as np
from inputs import goal, initialState

# number of nodes expanded
expanded = 0


# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory, expandNode



if __name__ == '__main__':
    pass

    print('DEPTH FIRST SEARCH')

    print('Goal:   ', getString(goal))
    
    # state is the state that will be acted upon
    state = np.copy(initialState)
    
    print('Init:   ', getString(initialState))
    
    
    # create a list of nodes with the initial node as the first element
    frontier = []
    frontier.append(state)
    print('added:  ', getString(state))
    
    # history of nodes that have been in frontier
    history = []
    
    # loop through the frontier
    while(frontier):
        # pop out last node
        node = frontier.pop(-1)
        expanded += 1
        
        print('popped: ', getString(node))
        
        # add node to history
        history.append(node)
        
        # test if success
        if(testGoal(node)):
            print('Reached successful node!')
            break;
        
        # expand node 
        frontier, history = expandNode(node, frontier, history)

    
    # print info
    print('Number of nodes in fringe: ', len(frontier))
    print('Number of nodes expanded: ', expanded)













