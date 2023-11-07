#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: wes
Created: Thu Sep 30 05:51:28 PDT 2021

Description: this code generates a 2D "heatmap" style plot using sample data that
is hard-coded into the code.

Inputs: none, all problem parameters are hard-coded.

Outputs: a plot showing the heatmap, displayed to the screen

Dependencies: matplotlib, numpy

Assumptions: Developed and Tested with Python 3.8.8 on MacOS 11.6
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

threads_per_block = ['32', '64', '128', '256', '512', '1024'] # y axis, 6 of them
thread_blocks = ["1", "4", "16", "64", "256", "1024", "4096"] # x axis, 7 of them

# runtime = np.array([[3.25, 0.82813,0.22139,0.06204, 0.02106, 0.02106, 0.02108],
#                     [1.65, 0.428,0.12173,0.04167, 0.02510, 0.02506, 0.02498],
#                     [0.85545, 0.2286,0.06389,0.02150, 0.02631, 0.02634, 0.02646],
#                     [0.52474, 0.14577, 0.05135,0.02580, 0.04069, 0.04072, 0.04071],
#                     [0.39662, 0.11452,0.03842,0.03841, 0.07232, 0.07232, 0.07225],
#                     [0.39191, 0.14896,0.07502,0.07494, 0.07489, 0.07494, 0.07498]])

# aoccupancy = np.array([[1.56, 1.56, 1.56, 1.56, 2.33, 3.10, 3.10],
#                        [3.11, 3.11, 3.11, 3.10, 4.03, 5.77, 5.83],
#                        [6.15, 6.14, 6.13, 6.13, 11.28, 11.72, 11.98],
#                        [12.04, 12.04, 12.03, 12.02, 21.02, 21.03, 21.03],
#                        [23.55, 23.53, 23.51, 23.51, 37.44, 37.44, 37.42],
#                        [43.91, 43.91, 43.84, 43.85, 43.86, 43.81, 43.81]])

memw = np.array([[0.01, 0.02, 0.09, 0.31, 0.92, 0.90, 0.91],
                 [0.01, 0.05, 0.16, 0.46, 0.78, 0.77, 0.77],
                 [0.02, 0.08, 0.30, 0.89, 0.73, 0.73, 0.73],
                 [0.04, 0.12, 0.37, 0.75, 0.45, 0.47, 0.47],
                 [0.05, 0.17, 0.50, 0.50, 0.26, 0.26, 0.27],
                 [0.05, 0.13, 0.25, 0.26, 0.25, 0.26, 0.25]])
#     1, 4, 16, 64, 256, 1024, 4096
# 32, 
# 64, 
# 128, 
# 256, 
# 512, 
# 1024


fig, ax = plt.subplots()
im = ax.imshow(memw, cmap="coolwarm")

# We want to show all ticks...
ax.set_xticks(np.arange(len(thread_blocks)))
ax.set_yticks(np.arange(len(threads_per_block)))
# ... and label them with the respective list entries
ax.set_xticklabels(thread_blocks)
ax.set_yticklabels(threads_per_block)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(threads_per_block)): # y axis
    for j in range(len(thread_blocks)): # x axis
        text = ax.text(j, i, round(memw[i, j],2),
                       ha="center", va="center", color="k")

ax.set_title("Peak Mem-Bw(%) at Varying Block Sizes and Threads, A100")
ax.set_ylabel('Threads per block')
ax.set_xlabel('Block Sizes')
fig.colorbar(im, ax=ax)
fig.tight_layout()
plt.show()

# EOF
