import matplotlib.pyplot as plt
import math
import numpy as np


def draw(data, data2):
    xData = []
    yData = []
    xData2 = []
    yData2 = []
    for i in range(len(data)):
        xData.append(math.log10(i + 1))
        yData.append(math.log10(data[i]))
    for i in range(len(data2)):
        xData2.append(math.log10(i + 1))
        yData2.append(math.log10(data2[i]))
    plt.plot(xData, yData, c = 'blue')
    plt.plot(xData2, yData2, c = 'red')
    plt.xlabel('log rank')
    plt.ylabel('log cf')
    plt.grid()
    plt.show()

with open('5000simple_zipf.txt') as f:
    lines = f.read().splitlines()
for i in range(len(lines)):
    lines[i] = int(lines[i])
with open('5000pro_zipf.txt') as f:
    lines2 = f.read().splitlines()
for i in range(len(lines2)):
    lines2[i] = int(lines2[i])
draw(lines, lines2)