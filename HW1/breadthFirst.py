'''
Created on Feb 6, 2018

@author: dabrown
'''

import numpy as np


# This is the initial goal of the program
goal = np.array(['*','1','2','3','4','5','6','7','8'])

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

if __name__ == '__main__':
    pass

    
    print('Goal: ', getString(goal))
    
    # This generates an initial random state for the program
    # state is the state that will be acted upon
    initialState = np.copy(goal)
    np.random.shuffle(initialState)
    state = np.copy(initialState)
    
    print('Initial State: ', getString(initialState))
    
    
    # create a list of nodes with the initial node as the first element
    frontier = []
    frontier.append(state)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    