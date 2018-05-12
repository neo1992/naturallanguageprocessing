import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import numpy as np

style.use("dark_background")

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.xlabel('Time')
plt.ylabel('Sentiment')


def animate(i):
    pullData = open("twitter_out.txt", "r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0


    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar, yar)


ani = animation.FuncAnimation(fig, animate, interval=20, frames=200)
plt.show()