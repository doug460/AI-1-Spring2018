'''
Created on Feb 6, 2018

@author: dabrown
'''

import numpy as np
from inputs import goal, initialState

# imports from breadthFirst search
from breadthFirst import getString, testGoal, testHistory, NewNode

# number of nodes expanded
expanded = 0



# heuristic for misplaced tiles
# input:
#     the array to compare with the goal
# output:
#     number of misplaced tiles
def misplaced(array):
    return len(goal) - np.sum(array == goal)

# heuristic for Manhattan distance
# input:
#     array for getting Manhattan distance 
# output:
#     sum of distances
def manhat(array):
    # total distance of moves
    totalDistance = 0
    
    # loop through each element
    for indx, element in enumerate(array):
        # distance for each element
        distance = 0
        
        # dont count * as a tile
        if(element != '*'):
            # get which layer element is in 
            if(indx == 0 or indx == 1 or indx == 2):
                layer = 0
            elif(indx == 3 or indx == 4 or indx == 5):
                layer = 1
            else:
                layer = 2
        
            # get the goal layer for element
            goalIndx = np.where(goal==element)[0][0]
            
            # get which layer goal is  
            if(goalIndx == 0 or goalIndx == 1 or goalIndx == 2):
                goalLayer = 0
            elif(goalIndx == 3 or goalIndx == 4 or goalIndx == 5):
                goalLayer = 1
            else:
                goalLayer = 2
                
            # while they layers are not the same, move element
            while(layer != goalLayer):
                # shift up or down to get to correct layer and count moves
                if(layer > goalLayer):
                    indx -= 3
                    layer -= 1
                    distance += 1
                else:
                    indx += 3
                    layer += 1
                    distance += 1
                    
            # now on correct layer, get remaining moves
            distance += abs(indx - goalIndx)
            
            # update total distance
            totalDistance += distance
    
    return totalDistance

# quickly get the cost
def getCost(array):
    return(manhat(array) + misplaced(array))


# expand a node excluding previous states
# input:
#     node array
#     frontier list
#     history of expanded nodes list
# output:
#    updated frontier
#    updated history
def expandNode(node, frontier, history):
    # get index of where the blank space is at
    index = np.where(node.array=='*')[0][0]
    
    # holds the node to be added to the list
    
    
    # check above empty
    if(index - 3 >= 0):
        # switch positions
        nextNode = np.copy(node.array)
        nextNode[index] = node.array[index - 3]
        nextNode[index - 3] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(NewNode(nextNode,node))
            history.append(nextNode)
            print('added:   %s cost: %d' % (getString(nextNode), getCost(nextNode)))
        
    # check below empty
    if(index + 3 <= 8):
        # switch positions
        nextNode = np.copy(node.array)
        nextNode[index] = node.array[index + 3]
        nextNode[index + 3] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(NewNode(nextNode,node))
            history.append(nextNode)
            print('added:   %s cost: %d' % (getString(nextNode), getCost(nextNode)))
    
    # check left empty
    if(index != 0 and index != 3 and index != 6):
        # switch positions
        nextNode = np.copy(node.array)
        nextNode[index] = node.array[index - 1]
        nextNode[index - 1] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(NewNode(nextNode,node))
            history.append(nextNode)
            print('added:   %s cost: %d' % (getString(nextNode), getCost(nextNode)))
    
    # check right empty
    if(index != 2 and index != 5 and index != 8):
        # switch positions
        nextNode = np.copy(node.array)
        nextNode[index] = node.array[index + 1]
        nextNode[index + 1] = '*'
        
        # add to frontier if not already explored
        if(not testHistory(nextNode, history)):
            frontier.append(NewNode(nextNode,node))
            history.append(nextNode)
            print('added:   %s cost: %d' % (getString(nextNode), getCost(nextNode)))
            
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
    




















