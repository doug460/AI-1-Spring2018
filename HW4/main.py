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
LOSE = 3

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
    # prohibited numbers 
    
    def __init__(self, parent, player, num, prohibited):
        self.parent = parent
        self.player = player
        self.num = num
        self.prohibited = prohibited
        print(num)
        print(prohibited)
        

def expandNode(node,player):
    # switch players and expand node
    
    # switch players
    if player == A:
        player = B
    else:
        player = A
    
    # available nodes left
    nodes = []
            
    
    
        
    


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
        # prohibited numbers for this node
        prohibited = []
        for row in edges:
            if row[0] == num:
                prohibited.append(row[1])
            if row[1] == num:
                prohibited.append(row[0])
        
        node = Node(None, player, num, prohibited)
        nodes.append(node)
    
#     # to wonder land
#     for node in nodes:
#         result = expandNode(node, player)
    
    
    
    
























    
    