README

Doug Brown
3-2-18

assuming python 2.7


----------- COMPILE ------------
All files need to be in same folder

Given input file 'foo.txt', the following commands are run to run each algorithm respectively

	python breadthFirst.py foo.txt
	python depthFirst.py foo.txt
	python iterativeDeepening.py foo.txt
	python aStar.py foo.txt
	
----------- Example inputs ----------
Test inputs
The mapping of the numbers is shown on the testMaps.jpg

Test 2 is not solveable

The rest are solveable

Additionally the US map is included.
The layout is under usLayout.txt and the corresponding map is usNumberedMap.jpg


---------- Code ----------
each of the codes run as expected from the previous lab (i.e. breadthfirst is a breadthfirst search algorithm


----------- Heuristics -------------
for A*, the heuristic is based on the colors
To save the number of colors used the cost is minimized if more colors can be repeated