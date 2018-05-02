'''
Created on May 1, 2018

@author: dabrown

main program to run the searching algorithm to solve the coloring graph
'''

import numpy as np
import fileinput


# get input file from user
fileIn = fileinput.input()
# need to read one line to get name of file
trash = next(fileIn)
fileName = fileIn.filename()
fileIn.close()

# keep track of players
A = 1
B = 2

# win lose or tie
WIN = 1
TIE = 2
LOSS = 3

# get input nodes 
edgeNum = None;
edges = [];
nodeNum = None;


def getInputs():
    global nodeNum, edges, edgeNum
    #******#
    # Get inputs is for importing information about color map
    # input:
    #     None
    # output:
    #     edgesNum: number of edges
    #     edges:     the edges

    # edges is array to hold the edges in the graph
    
    # with resources get input
    with open(fileName) as file:
        
        # first get number of nodes
        edgeNum = int(next(file).split()[0])
        
        # read in all the edges
        for indx in range(edgeNum):
            array = next(file).split()
            edges.append([int(array[0]), int(array[1])])
            
        nodeNum = np.max(edges)

class Node:
    # nodes
    # parent node
    # player that colors this node
    # number of node
    # nodes left for A
    # nodes left for B
    # total nodes left on graph
    
    def __init__(self, parent, player, num, leftA, leftB, leftTot):
        self.parent = parent
        self.player = player
        self.num = num
        self.leftA = leftA
        self.leftB = leftB
        self.leftTot = leftTot
    
def reduceNode(node, player):
    # INPUT:
    #     node: single node
    #     player: which player chose these nodes
    # OUTPUT:
    #    result: win, lose, tie
    
    # this procedure reduces the list of nodes
    # recursive loop until no more options
    # you can think of this as moving down the search tree
    
    # alternate player that is playing
    if player == A:
        player = B
    else:
        player = A

    #keep list of results from each node
    # new list of nodes for next layer
    newNodes = []  
    
    # there are no positions left..., its a tie
    if not node.leftTot:
        return TIE, node
    
    # generate new nodes if possible
    if player == A:
        # update whats left
        for num in node.leftA:
            leftA = node.leftA[:]
            leftA = checkEdge(num, leftA)
            
            leftB = node.leftB
            if num in node.leftB:
                leftB = node.leftB[:]
                leftB.remove(num)
            leftTot = node.leftTot[:]
            leftTot.remove(num)
            newNodes.append(Node(node, player, num, leftA, leftB, leftTot))
    else:
        # update whats left for B
        for num in node.leftB:
            leftB = node.leftB[:]
            leftB = checkEdge(num, leftB)
            
            leftA = node.leftA
            if num in node.leftA:
                leftA = node.leftA[:]
                leftA.remove(num)
            leftTot = node.leftTot[:]
            leftTot.remove(num)
            newNodes.append(Node(node, player, num, leftA, leftB, leftTot))
            
    # now step through all new nodes
    # search down new node
    if newNodes:
        results = []
        retNodes = []
        for newNode in newNodes:
            # recursively explore new node
            result, retNode = reduceNode(newNode, player)
            results.append(result)
            retNodes.append(retNode)
        
        # choice in logic for the agents min-max
        # this is the min/max function
        # if player A, chose win -> tie -> loss
        # if player B, chose loss -> tie -> win
        if player == A:
            if WIN in results:
                indx = results.index(WIN)
                return WIN, retNodes[indx]
            elif TIE in results:
                indx = results.index(TIE)
                return TIE, retNodes[indx]
            else: 
                indx = results.index(LOSS)
                return LOSS, retNodes[indx]
        if player == B:
            if LOSS in results:
                indx = results.index(LOSS)
                return LOSS, retNodes[indx]
            elif TIE in results:
                indx = results.index(TIE)
                return TIE, retNodes[indx]
            else:
                indx = results.index(WIN)
                return WIN, retNodes[indx]
    
    # if no new nodes then either player A wins or losses. 
    # TIE  has already been covered in the initial part of this function
    else:
        if player == A:
            return LOSS, node
        else:
            return WIN, node
            
        
def checkEdge(num, left):
    # INPUT:
    #    num: is the number of the current node chosen
    #    left: list of numbers left to chose from
    # OUTPUT:
    #     left: updated nodes left
    
    # step through each edge
    for edge in edges:
        # step through each number
        # if number has constraint, make sure contraint number is no longer allowed
        if num in edge:
            # make sure new number is removed from what is left for that player
            if edge[0] in left:
                left.remove(edge[0])
            if edge[1] in left:
                left.remove(edge[1])
            
    return(left)

def printMoves(node):
    # INPUT:
    #    node: get node and print moves taken by each player
    # recursive to print from top of node branch
    parent = node.parent
    if parent:
        printMoves(node.parent)
    
    if(node.player == A):
        print('A: %d' % (node.num))
    else:
        print('B: %d' %(node.num))
    
    


if __name__ == '__main__':
    pass

    # get inputs
    getInputs() 
    
    # first player is A
    player = A
    
    # final results of initial nodes
    nodes = []
    results = []
    
    
    # create an initial node for each possible start position for A
    for num in range(1,nodeNum+1):
        # list of nodes left for A and for B
        leftB = list(range(1,nodeNum + 1))
        leftA = list(range(1,nodeNum + 1))
        leftTot = list(range(1,nodeNum+1))
        
        # num is no longer available as player A has taken that position
        leftA.remove(num)
        leftB.remove(num)
        leftTot.remove(num)
        
        # update leftA based on edges
        leftA = checkEdge(num, leftA)
        
        # generate node and go into node exploration/reduction
        node = Node(None, player, num, leftA, leftB, leftTot)
        result, node = reduceNode(node,player)
        
        # keep list of solutions and nodes
        results.append(result)
        nodes.append(node)
        
    # of the results, chose the option that best suits player A    
    # if there is a win
    if WIN in results:
        indx = results.index(WIN)
        node = nodes[indx]
        print('PLAYER A WINS')
        print('Moves:')
        printMoves(node)
        
    elif TIE in results:
        indx = results.index(TIE)
        node = nodes[indx]
        print('PLAYERS TIE')
        print('Moves:')
        printMoves(node)
        
    else:
        indx = results.index(LOSS)
        node = nodes[indx]
        print('PLAYER A LOSSES')
        print('Moves:')
        printMoves(node)
    
























    
    