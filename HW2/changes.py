'''
Created on Mar 4, 2018

@author: DougBrownWin

This has all the chages in one file
'''

####################################################################################################

# is value of no color
noColor = 0

#*****#
# test if the state is a solution
# input:
#     Array
# Output:
#    boolean
def testGoal(array):
    return(not (noColor in array))


####################################################################################################


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

####################################################################################################


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
        for color in range(1,colorsNum + 1):
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


####################################################################################################

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

####################################################################################################


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

####################################################################################################


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
    

####################################################################################################

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