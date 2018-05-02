'''
Created on May 1, 2018

@author: dabrown

main program to run the searching algorithm to solve the coloring graph
'''

import numpy as np
import fileinput
from scipy.stats.stats import tiecorrect


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
    # recurisive loop until no more options
    
    # alternate player
    if player == A:
        player = B
    else:
        player = A

    #keep list of results from each node
    # new list of nodes for next layer
    newNodes = []  
    
    # there are no positions left..., its a tie
    if not node.leftTot:
        return TIE
    
    # generate new nodes
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
    if newNodes:
        results = []
        for newNode in newNodes:
            results.append(reduceNode(newNode, player))
        
        # choice in logic for the agents min-max
        if player == A:
            if WIN in results:
                return WIN
            elif TIE in results:
                return TIE
            else: 
                return LOSS
        if player == B:
            if LOSS in results:
                return LOSS
            elif TIE in results:
                return TIE 
            else:
                return WIN
    
    # if no new nodes
    else:
        if player == A:
            return LOSS
        else:
            return WIN
            
        
def checkEdge(num, left):
    # INPUT:
    #    num: is the number of the current node chosen
    #    left: list of numbers left to chose from
    # OUTPUT:
    #     left: updated nodes left
    
    for edge in edges:
        if num in edge:
            if edge[0] in left:
                left.remove(edge[0])
            if edge[1] in left:
                left.remove(edge[1])
            
    return(left)


if __name__ == '__main__':
    pass

    # get inputs
    getInputs() 
    
    # first player is A
    player = A
    
    # initialize stuff
    nodes = []
    # keep track of nodes
    
    
    
    for num in range(1,nodeNum+1):
        # list of nodes left for A and for B
        leftB = list(range(1,nodeNum + 1))
        leftA = list(range(1,nodeNum + 1))
        leftTot = list(range(1,nodeNum+1))
        
        # num is no longer available
        leftA.remove(num)
        leftB.remove(num)
        leftTot.remove(num)
        
        # update leftA based on edges
        leftA = checkEdge(num, leftA)
        
        node = Node(None, player, num, leftA, leftB, leftTot)
        result = reduceNode(node,player)
        print(result)
    
    
























    
    