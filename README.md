# Biometrics Project 1

This is project 1 for CSE491 Biometrics. This program was written in python and can be executed using the command `python [filename]`.

## Evaluate scores

Execute `python evaluateScores.py` to run the score evaluation code.

#### Expected output

```
Finger
------------------
Minimum score: 0
Maximum score: 966


Scores for: Genuine Finger
Mean: 157.0
Variance: 42750.0


Scores for: Imposter Finger
Mean: 7.0
Variance: 91.0


D-Prime: 1.02488811537


------------------


FMR: 0.0422222222222
FNMR: 0.0933333333333

Hand
------------------
Minimum score: 0
Maximum score: 626


Scores for: Genuine Hand
Mean: 97.0
Variance: 6420.0


Scores for: Imposter Hand
Mean: 144.0
Variance: 6925.0


D-Prime: 0.575378416538


------------------


FMR: 0.00444444444444
FNMR: 0.448888888889

```

## Render graphs

Execute `python render.py` to render the histograms and ROC curves for the finger and face matcher. The graphs will be displayed one at a time and are labeled to make grading easier.

### Expected output

![Finger Score Distribution](https://dl.dropboxusercontent.com/u/717136/cse491/facescores.png)

![Finger Score Distribution](https://dl.dropboxusercontent.com/u/717136/cse491/fingerscores.png)

![Finger Score Distribution](https://dl.dropboxusercontent.com/u/717136/cse491/faceroc.png)

![Finger Score Distribution](https://dl.dropboxusercontent.com/u/717136/cse491/fingerroc.png)




