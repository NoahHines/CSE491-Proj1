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

def getScores(title, filename):
	scores = [int(float(line.rstrip('\n'))) for line in open(filename+".score")]
	quicksort(scores, 0, len(scores)-1)
	return scores

def displayHistogram(gen, imp, title):
    bins = np.linspace(0, 100, 100)
    plt.title(title)
    plt.hist(gen, bins, alpha=0.5, label='Genuine')
    plt.hist(imp, bins, alpha=0.5, label='Imposter')
    plt.legend(loc='upper right')
    plt.show()

def displayROC(gen, imp, title, isSim):
    x = gen
    y = imp
    # Only works if there are equal number of scores in gen and imp
    if (isSim == 1):
        for i in range(0, 450):
            x[i] = getSimFMR(i, imp)
            y[i] = getSimFNMR(i, gen)
            if (x[i] == y[i]):
                eer = x[i]
    else:
        for i in range(0, 450):
            x[i] = getDistFMR(i, imp)
            y[i] = getDistFNMR(i, gen)
            if (x[i] == y[i]):
                eer = x[i]
    plt.title(title + " (EER = " + str(eer) + ")")
    plt.scatter(x, y)
    plt.plot(eer)
    P.ylim([0,1])
    P.xlim([0,1])
    plt.show()
    return eer

# Finger histogram
gen = getScores("finger", "scores/finger_genuine")
imp = getScores("finger", "scores/finger_impostor")
displayHistogram(gen, imp, "Finger Scores")

# Hand histogram
gen = getScores("finger", "scores/hand_genuine")
imp = getScores("finger", "scores/hand_impostor")
displayHistogram(gen, imp, "Hand Scores")

gen = getScores("finger", "scores/finger_genuine")
imp = getScores("finger", "scores/finger_impostor")
eer = displayROC(gen, imp, "Finger ROC", 1)
print "Equal Error Rate (EER) = " + str(eer)

gen = getScores("finger", "scores/hand_genuine")
imp = getScores("finger", "scores/hand_impostor")
eer = displayROC(gen, imp, "Face ROC", 0)
print "Equal Error Rate (EER) = " + str(eer)


