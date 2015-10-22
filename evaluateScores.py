'''
Noah Hines
CSE491 Biometrics
Project 1
'''

# import numpy as np
# import matplotlib.pyplot as plt
import math

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

def getMean(scores):
    totalSum = 0
    for i in scores:
        totalSum += i
    return str(float(totalSum/(len(scores))))

def getVariance(mean, scores):
    totalSquaredSum = 0
    for i in scores:
        totalSquaredSum += ((i-mean)*(i-mean))
    return str(float(totalSquaredSum/(len(scores))))

# Mean is calculated before. stdDev is just variance^2
def getDPrime(mean1, mean2, stdDev1, stdDev2):
    return str(float( (math.sqrt(2)*abs(mean1-mean2)) / (math.sqrt(stdDev1 + stdDev2)) ) )


def getScores(title, filename):
	scores = [int(float(line.rstrip('\n'))) for line in open(filename+"_genuine.score")]
	quicksort(scores, 0, len(scores)-1)
    	print("\n" + title + "\n------------------")
	print("Scores for: Genuine " + title)
	print("Minimum score: " + str(scores[0]))
	print("Maximum score: " + str(scores[len(scores)-1]))
	genMean = getMean(scores)
	print("Mean: " + genMean)
    	genVariance = getVariance(int(float(genMean)), scores)
    	print("Variance: " + genVariance)

    	scores = [int(float(line.rstrip('\n'))) for line in open(filename+"_impostor.score")]
    	quicksort(scores, 0, len(scores)-1)
        print("\n");
    	print("Scores for: Imposter " + title)
    	print("Minimum score: " + str(scores[0]))
    	print("Maximum score: " + str(scores[len(scores)-1]))
    	impMean = getMean(scores)
   	print("Mean: " + impMean)
    	impVariance = getVariance(int(float(impMean)), scores)
    	print("Variance: " + impVariance)
        print("\n")
    	print("D-Prime: " + getDPrime(float(genMean), float(impMean), float(genVariance), float(impVariance)))
	print("------------------\n")

getScores("Finger", "scores/finger")
getScores("Face", "scores/hand")




