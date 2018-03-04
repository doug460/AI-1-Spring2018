'''
Created on Feb 6, 2018

@author: dabrown
'''
import numpy as np

# number of nodes expanded
expanded = 0


# keep track of nodes in current layer and next layer
currentLayer_nodes = 0
nextLayer_nodes = 0

# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory, NewNode, expandNode, getInputs



if __name__ == '__main__':
    pass

    print('ITERATIVE DEEPENING SEARCH')
    
    print('\nThe output array is the color associated with each state')
    print('0 means no assigned color\n')
    
    # get inputs
    statesNum, edgesNum, colorsNum, edges = getInputs()
    
    # get colors for each state
    # initially all are undecided
    colors = np.zeros((statesNum), dtype = np.int32)
    
    # limit for how far the current level is allowed to go down in depth
    # this iteratively increases
    depthLimit = 0
    
    # success in depth
    success = False
    
    # how many nodes were expanded previously
    expandedNodes_prev = 0
    
    
    # infinite loop for deepening
    # as long as new nodes are indeed created
    while(not success):
        # reset current depth
        depthLeft = depthLimit
        
        # create a list of nodes with the initial node as the first element
        frontier = []
        frontier.append(NewNode(colors, None))
        print('added:   %s' % (getString(colors)))
        currentLayer_nodes += 1
        
        # history of nodes that have been in frontier
        history = []
        
        # keep track of the number of nodes that were expanded
        expandedNodes = expanded
        
        # loop through the frontier
        while(frontier):
            # pop out first node
            node = frontier.pop(-1)
            expanded += 1
            currentLayer_nodes -= 1
            
            print('popped:  %s' %( getString(node.array)))
            
            # add node to history
            history.append(node.array)
            
            # test if success
            if(testGoal(node.array)):
                success = True
                print('## Reached successful node! ##')
                break;
            
            # expand node 
            if(depthLeft > 0):
                frontier, history = expandNode(node, frontier, history, colorsNum, edges)
                
            # check when reached in of layer
            # update current and next layer nodes
            if(currentLayer_nodes == 0):
                currentLayer_nodes = nextLayer_nodes
                nextLayer_nodes = 0
                depthLeft -= 1
                
        print('-- Finished this layer --')
        
        # increase depth    
        depthLimit += 1
        
        # how many nodes were created this round
        expandedNodes = expanded - expandedNodes
        
        # if there is not a difference between previously expanded nodes and current expanded nodes
        # than increasing the depth did not help and should terminate
        if(expandedNodes == expandedNodes_prev and not success):
            print('\nIncreasing depth did not help... terminating program')
            break;
        else:
            expandedNodes_prev = expandedNodes
        
    
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
            
    




    