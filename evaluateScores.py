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

def getSimFMR(threshold, scores):
    totalSum = 0.0
    for i in scores:
        if (i >= threshold):
            totalSum += 1
    # print "totalSum: " + str(totalSum)
    return (totalSum/float(len(scores)))

def getSimFNMR(threshold, scores):
    totalSum = 0.0
    # print "Score length: " + str(len(scores))
    for i in scores:
        if (i < threshold):
            totalSum += 1
            # print str(i)
    # print "totalSum: " + str(totalSum)
    return (totalSum/float(len(scores)))

def getDistFMR(threshold, scores):
    totalSum = 0.0
    for i in scores:
        if (i < threshold):
            totalSum += 1
    # print "totalSum: " + str(totalSum)
    return (totalSum/float(len(scores)))

def getDistFNMR(threshold, scores):
    totalSum = 0.0
    # print "Score length: " + str(len(scores))
    for i in scores:
        if (i >= threshold):
            totalSum += 1
            # print str(i)
    # print "totalSum: " + str(totalSum)
    return (totalSum/float(len(scores)))

def getScores(title, filename, threshold):
	gen = [int(float(line.rstrip('\n'))) for line in open(filename+"_genuine.score")]
	imp = [int(float(line.rstrip('\n'))) for line in open(filename+"_impostor.score")]
	totalScores = gen
    	totalScores.extend(imp)
	quicksort(gen, 0, len(gen)-1)
    	quicksort(imp, 0, len(imp)-1)
    	quicksort(totalScores, 0, len(totalScores)-1)
    	print("\n" + title + "\n------------------")
        print("Minimum score: " + str(totalScores[0]))
   	print("Maximum score: " + str(totalScores[len(totalScores)-1]))
    	print("\n")
	print("Scores for: Genuine " + title)
	genMean = getMean(gen)
	print("Mean: " + genMean)
    	genVariance = getVariance(int(float(genMean)), gen)
    	print("Variance: " + genVariance)
    	quicksort(imp, 0, len(imp)-1)
        print("\n");
    	print("Scores for: Imposter " + title)
    	impMean = getMean(imp)
   	print("Mean: " + impMean)
    	impVariance = getVariance(int(float(impMean)), imp)
    	print("Variance: " + impVariance)
        print("\n")
    	print("D-Prime: " + getDPrime(float(genMean), float(impMean), float(genVariance), float(impVariance)))
        print("\n")
        print("------------------\n\n")

getScores("Finger", "scores/finger", 32.0)
filename = "scores/finger"
threshold = 32
gen = [int(float(line.rstrip('\n'))) for line in open(filename+"_genuine.score")]
imp = [int(float(line.rstrip('\n'))) for line in open(filename+"_impostor.score")]
print("FMR: " + str(getSimFMR(threshold, imp)))
print("FNMR: " + str(getSimFNMR(threshold, gen)))

getScores("Hand", "scores/hand", 45.0)
filename = "scores/hand"
threshold = 45
gen = [int(float(line.rstrip('\n'))) for line in open(filename+"_genuine.score")]
imp = [int(float(line.rstrip('\n'))) for line in open(filename+"_impostor.score")]
print("FMR: " + str(getDistFMR(threshold, imp)))
print("FNMR: " + str(getDistFNMR(threshold, gen)))


