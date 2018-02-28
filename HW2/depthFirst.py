'''
Created on Feb 6, 2018

This is the depth-first search algorithm

The inputs are the initial state and the goal state, represented as arrays

The output are the nodes added to and popped from the frontier 

@author: dabrown
'''



import numpy as np

# number of nodes expanded
expanded = 0


# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory, expandNode, NewNode, getInputs



if __name__ == '__main__':
    pass

    print('DEPTH FIRST SEARCH')
    print('\nThe output array is the color associated with each state')
    print('0 means no assigned color\n')
    
    # get inputs
    statesNum, edgesNum, colorsNum, edges = getInputs()
    
    # get colors for each state
    # initially all are undecided
    colors = np.zeros((statesNum), dtype = np.int32)
    
    # create a list of nodes
    frontier = []
    
    # get node for first completely undecided system
    initialState = NewNode(colors, None)
    frontier.append(initialState)
    print('Initial state is ', getString(colors))
    
    # history of nodes that have been in frontier
    history = []
    
    # keep track if program was successful 
    success = False
    
    # loop through the frontier
    while(frontier):
        # pop out last node
        node = frontier.pop(-1)
        expanded += 1
        
        print('popped:  %s' %( getString(node.array)))
        
        # add node to history
        history.append(node.array)
        
        # test if success
        if(testGoal(node.array)):
            print('Reached successful node!')
            success = True
            break;
        
        # expand node 
        frontier, history = expandNode(node, frontier, history, colorsNum, edges)

    
    # whether or not the problem was solvable
    if(success):
        # print info
        print('Number of nodes in fringe: %d' % ( len(frontier)))
        print('Number of nodes expanded: %d' % ( expanded))
    
        # successful orientation is 
        print('\nSuccessful orientation is: %s' % (getString(node.array)))
    else:
        # was not successful
        print('Was not able to find a solution')
        print('Problem is not solvable!')












