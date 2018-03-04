'''
Created on Feb 6, 2018

@author: dabrown

uses both heuristics
'''

import numpy as np

# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory, NewNode, getInputs, noColor, passConstraint, nextLayer_nodes

# number of nodes expanded
expanded = 0

#********#
# input is the current color array
# the heuristic is simply want to use repeated colors
# INPUT:
#    array- just the current array of colors
# OUTPUT:
#     repeated- the number of times a color is repeated
def getCost(array):
    # count time a color is repeated
    repeated = 0
    for element in array:
        # exclude counted zeros
        if(element != 0):
            counted = (array == element).sum()
            # keep track of max
            if(counted > repeated):
                repeated = counted
    
    return -repeated


#******#
# expand a node excluding previous states
# input:
#     node 
#     frontier list
#     history of expanded nodes list
#     colorsNum
#     edges
# output:
#    updated frontier
#    updated history
def expandNode(node, frontier, history, colorsNum, edges):
    # get index of where the blank space is at
    array = node.array
    nextArray = np.copy(array)
    
    # keep track of nodes in layer
    global nextLayer_nodes
    
    
    # check if there is an unassigned color in array
    if(noColor in array):
        # get state index where the zero is at
        state = np.where(array == noColor)[0][0]          
        # step through and add colors
        for color in range(colorsNum + 1):
            nextArray = np.copy(array)
            nextArray[state] = color
            # if node doesn't exist in history
            if(not testHistory(nextArray, history)):
                # if new allowed color
                if(passConstraint(nextArray, edges)):
                    frontier.append(NewNode(nextArray, node))
                    history.append(nextArray)
                    print('added:   %s with cost %d' % (getString(nextArray), getCost(nextArray)))
                    nextLayer_nodes += 1
                 
            
    return(frontier, history)


# gets the index of the node that is the most optimal to be popped
# input:
#     list of nodes
# output:
#     index of optimal node
def aStar(frontier):
    minIndx = 0
    minCost = 0
    # loop through all the nodes
    for indx, node in enumerate(frontier):
        cost = getCost(node.array)
        
        # if first run
        if(indx == 0):
            minIndx = indx
            minCost = cost
            
        # if this cost is smaller, save index
        if(cost < minCost):
            minIndx = indx
            minCost = cost
            
    return(minIndx)
    
    

if __name__ == '__main__':
    pass

    print('A* SEARCH')
    
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
    
    # keep track of success
    success = False
    
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
        
        print('\nState: color')
        for state, color in enumerate(node.array):
            print('%d: %d' % (state + 1, color))
    else:
        # was not successful
        print('Was not able to find a solution')
        print('Problem is not solvable!')
        
        # print info
        print('Number of nodes in fringe: %d' % ( len(frontier)))
        print('Number of nodes expanded: %d' % (expanded))
    




















