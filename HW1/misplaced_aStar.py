'''
Created on Feb 6, 2018

@author: dabrown

uses only misplaced tiles heuristic
'''

import numpy as np
from inputs import goal, initialState

# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory, NewNode
from aStar import misplaced, manhat, expandNode, aStar

# number of nodes expanded
expanded = 0

# quickly get the cost
def getCost(array):
    return(misplaced(array))
    

if __name__ == '__main__':
    pass

    print('A* SEARCH')
    
    print('Goal:    %s' % (getString(goal)))
    
    # state is the state that will be acted upon
    state = np.copy(initialState)
    
    print('Init:    %s' % (getString(initialState)))
    
    
    # create a list of nodes with the initial node as the first element
    frontier = []
    frontier.append(NewNode(state,None))
    print('added:   %s cost: %d' % (getString(state), getCost(state)))
    
    # history of nodes that have been in frontier
    history = []
    
    # loop through the frontier
    while(frontier):
        # get the index of the optimal node
        indx = aStar(frontier)
        
        # pop optimal node
        node = frontier.pop(indx)
        expanded += 1
        
        print('popped:  %s' %( getString(node.array)))
        
        # add node to history
        history.append(node.array)
        
        # test if success
        if(testGoal(node.array)):
            print('Reached successful node!')
            break;
        
        # expand node 
        frontier, history = expandNode(node, frontier, history)
    
    # print info
    print('Number of nodes in fringe: %d' % ( len(frontier)))
    print('Number of nodes expanded: %d' % ( expanded))
    
    # path to solve problem (reverse order)
    path = []
    path.append(node)

    # get path
    while(node.parent != None):
        node = node.parent
        path.append(node)

    # print out path
    print('\nThe solution path is:')
    while(path):
        print(getString(path.pop(-1).array))
    




















