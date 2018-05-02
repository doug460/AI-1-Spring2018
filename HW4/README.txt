README for colringAgent

The general idea is to search down the tree following a min/max operation for switching between players A and B

RUN: to run the code, the python code takes a text input
	python colringAgent.py foo.txt

INPUT is in the form of a text file through the command line.
	The number of edges are stated
	Each edge is then stated in pairs
	
	!!!An EMPTY node MUST be given an empty edge. ie "1 0" is node 1 that is not connected to any other node


MIN/MAX priority is given as follows. Player A favors MAX, and player B favors MIN
	MAX priority: WIN, TIE, LOSS	
	MIN priority: LOSS, TIE, WIN


OUTPUT:
	States if player A can win. 
	An example of the best possible play for player A is given.
		The node that each player colors is stated
		
  