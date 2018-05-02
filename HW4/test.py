'''
Created on May 1, 2018

@author: dabrown
'''

import numpy as np

def loop():
    for indx in range(10):
        if(indx == 3):
            return indx

if __name__ == '__main__':
    pass

    list = ['here', 'five', 3, 'hi']
    list2 = [1,3, 4, 3]
    
    indx = list2.index(3)
    print(indx)
    print(list[indx])
    