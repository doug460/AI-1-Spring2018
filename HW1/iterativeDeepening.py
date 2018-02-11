'''
Created on Feb 6, 2018

@author: dabrown
'''
import numpy as np
from inputs import goal, initialState

# number of nodes expanded
expanded = 0


# keep track of nodes in current layer and next layer
currentLayer_nodes = 0
nextLayer_nodes = 0

# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory


# expand a node excluding previous states
# input:
#     node array
#     frontier list
#     history of expanded nodes list
# output:
#    updated frontier
#    updated history
def expandNode(node, frontier, history):
    global nextLayer_nodes
    
    # get index of where the blank space is at
    index = np.where(node=='*')[0][0]
    
    # holds the node to be added to the list
    
    
    # check above empty
    if(index - 3 >= 0):
        # switch positions
        nextNode = np.copy(node)
        nextNode[index] = node[index - 3]
        nextNode[index - 3] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(nextNode)
            history.append(nextNode)
            print('added:  ', getString(nextNode))
            nextLayer_nodes += 1
        
    # check below empty
    if(index + 3 <= 8):
        # switch positions
        nextNode = np.copy(node)
        nextNode[index] = node[index + 3]
        nextNode[index + 3] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(nextNode)
            history.append(nextNode)
            print('added:  ', getString(nextNode))
            nextLayer_nodes += 1
    
    # check left empty
    if(index != 0 and index != 3 and index != 6):
        # switch positions
        nextNode = np.copy(node)
        nextNode[index] = node[index - 1]
        nextNode[index - 1] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(nextNode)
            history.append(nextNode)
            print('added:  ', getString(nextNode))
            nextLayer_nodes += 1
    
    # check right empty
    if(index != 2 and index != 5 and index != 8):
        # switch positions
        nextNode = np.copy(node)
        nextNode[index] = node[index + 1]
        nextNode[index + 1] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(nextNode)
            history.append(nextNode)
            print('added:  ', getString(nextNode))
            nextLayer_nodes += 1
            
    return(frontier, history)



if __name__ == '__main__':
    pass

    print('ITERATIVE DEEPENING SEARCH')
    
    print('Goal:   ', getString(goal))
    
    # state is the state that will be acted upon
    state = np.copy(initialState)
    
    print('Init:   ', getString(initialState))
    
    # limit for how far the current level is allowed to go down in depth
    # this itereatively increases
    depthLimit = 0
    
    success = False
    
    # infinite loop for deepening
    while(not success):
        # reset current depth
        depthLeft = depthLimit
        
        # create a list of nodes with the initial node as the first element
        frontier = []
        frontier.append(state)
        print('added:  ', getString(state))
        currentLayer_nodes += 1
        
        # history of nodes that have been in frontier
        history = []
        
        # loop through the frontier
        while(frontier):
            # pop out first node
            node = frontier.pop(0)
            expanded += 1
            currentLayer_nodes -= 1
            
            print('popped: ', getString(node))
            
            # add node to history
            history.append(node)
            
            # test if success
            if(testGoal(node)):
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
        print('-- Number of nodes in fringe: ', len(frontier))
        print('-- Number of nodes popped: ', expanded)
        
        if(not success):
            print('\n -- Depth increased to %d -- \n\n' % (depthLimit))


    print('\nFinished iterative deepening search!!')





    