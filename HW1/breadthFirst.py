'''
Created on Feb 6, 2018

This is the breadth first search program for AI 1

The first two arguments are the main parts of this program
the goal and the initial state

@author: dabrown
'''

import numpy as np
from inputs import goal, initialState


# number of nodes expanded
expanded = 0


# this function turns the character array into an easily printed string
# input:
#    character array
# output:
#     string
def getString(array):
    # string to hold chars
    string = ""
    
    # get the character and index in the array
    for indx, char in enumerate(array):
        # append to string holder
        string += char
    
    return string

# test if the state is a solution
# input:
#     Array
# Output:
#    boolean
def testGoal(array):
    return np.array_equal(array,goal)

# test history
# if node exists in history, return true
# else false
# input:
#    node
#    history
# output
# boolean
def testHistory(node, history):
    for array in history:
        if(np.array_equal(node,array)):
            return(True)
    
    return(False)


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
            
    return(frontier, history)
    
    
    

if __name__ == '__main__':
    pass

    print('BREADTH FIRST SEARCH')
    
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
        # pop out first node
        node = frontier.pop(0)
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    