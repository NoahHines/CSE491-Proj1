'''
Noah Hines
CSE491 Biometrics
Project 1
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab as P

def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.
            
            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def quicksort(list, start, end):
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return




def getScores(title, filename):
	scores = [int(float(line.rstrip('\n'))) for line in open(filename+".score")]
	quicksort(scores, 0, len(scores)-1)
	print scores
	print "\n\n"
	return scores


gen = getScores("finger", "scores/hand_genuine")
imp = getScores("finger", "scores/hand_impostor")

bins = np.linspace(0, 100, 100)

plt.hist(gen, bins, alpha=0.5, label='x')
plt.hist(imp, bins, alpha=0.5, label='y')
plt.legend(loc='upper right')
plt.show()

