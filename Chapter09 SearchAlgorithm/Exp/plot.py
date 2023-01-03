import numpy as np
import matplotlib.pyplot as plt

# First-choice hill climbing
x1 = np.arange(14140)  # numEval = 14140 when limitStuck = 1000
y1 = []
infile = open("resultFC.txt", 'r')
for line in infile:
    y1.append(float(line))
infile.close()    

# Simulated annealing
x2 = np.arange(61500)  # whenBestFound = 61260 when limitEval = 100000
y2 = []
infile = open("resultSA.txt", 'r')
for line in infile:
    y2.append(float(line))
infile.close()

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlabel('Number of Evaluations')
plt.ylabel('Tour Cost')
plt.title('Search Performance (TSP-100)')

# Legend elements are in the order of the above plots
plt.legend(['First-Choice HC', 'Simulated Annealing'])

plt.show()
