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
from breadthFirst import getString, testGoal, testHistory, NewNode, expandNode



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
    
    success = False
    
    # infinite loop for deepening
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
        
        # loop through the frontier
        while(frontier):
            # pop out first node
            node = frontier.pop(0)
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
                frontier, history = expandNode(node, frontier, history)
                
            # check when reached in of layer
            # update current and next layer nodes
            if(currentLayer_nodes == 0):
                currentLayer_nodes = nextLayer_nodes
                nextLayer_nodes = 0
                depthLeft -= 1
                
                print('-- Finished this layer --')
            
        depthLimit += 1
        
        # print info
        print('Number of nodes in fringe: %d' % ( len(frontier)))
        print('Number of nodes expanded: %d' % ( expanded))
        
        if(not success):
            print('\n -- Depth increased to %d -- \n\n' % (depthLimit))


    print('\nFinished iterative deepening search!!')
    
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





    