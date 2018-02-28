'''
Created on Feb 6, 2018

This is the breadth first search program for AI 1

The first two arguments are the main parts of this program
the goal and the initial state

@author: dabrown
'''

import numpy as np
import fileinput


# get input file from user
fileIn = fileinput.input()
# need to read one line to get name of file
trash = next(fileIn)
fileName = fileIn.filename()
fileIn.close()


# number of nodes expanded
expanded = 0

# is value of no color
noColor = 0

# keep track of nodes in layer
nextLayer_nodes = 0


# this function turns the character array into an easily printed string
# input:
#    character array
# output:
#     string
def getString(array):
    # string to hold chars
    string = ""
    
    # get the character and index in the array
    for value in array:
        # append to string holder
        temp = '%d' % (value)
        string += temp
    
    return string

#*****#
# test if the state is a solution
# input:
#     Array
# Output:
#    boolean
def testGoal(array):
    if noColor in array:
        return False
    else:
        return True

# test history
# if node exists in history, return true
# else false
# input:
#    arrayIn
#    history
# output
# boolean
def testHistory(arrayIn, history):
    for array in history:
        if(np.array_equal(arrayIn,array)):
            return(True)
    
    return(False)

#*****#
# check if it passes the constrains based on edges
# inputs:
#     array: array of colors that is proposed
#     edges:    edges in system
# output:
#     Boolean: true if allowed new node
def passConstraint(array, edges):
    
    # check all edges
    for edge in edges:
        pair = array[edge]
        # ignore if contains -1, thats and empty slot
        if(noColor not in pair):
            
            # if colors are same return false
            if(pair[0] == pair[1]):
                return False
    
    return True
    

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
                    print('added:   %s' % (getString(nextArray)))
                    nextLayer_nodes += 1
                 
            
    return(frontier, history)
    
#******#
# this is a node class
class NewNode:
    def __init__(self,array,parent):
        self.array = array
        self.parent = parent

#******#
# Get inputs is for importing information about color map
# input:
#     None
# output:
#     nodesNum: number of nodes
#     edgesNum: number of edges
#     colorsNum: number of colors
#     edges:     the edges
def getInputs():
    # edges is array to hold the edges in the graph
    edges = []
    
    # with resources get input
    with open(fileName) as file:
        # first get nodes, edges, and colors number
        statesNum, edgesNum, colorsNum = [int(x) for x in next(file).split()]
        
        # read in all the edges
        for indx in range(edgesNum):
            array = next(file).split()
            edges.append([int(array[0]) - 1, int(array[1]) - 1])
    
    # return info
    return(statesNum, edgesNum, colorsNum, edges)
    

if __name__ == '__main__':
    pass

    print('BREADTH FIRST SEARCH')   
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
    
    # keeps track if it was successful
    success = False
    
    # loop through the frontier
    while(frontier):
        # pop out first node
        node = frontier.pop(0)
        expanded += 1
        
        print('popped:  %s' %( getString(node.array)))
        
        # add node to history
        history.append(node.array)
        
        # test if success
        if(testGoal(node.array)):
            print('\nReached successful node!')
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
