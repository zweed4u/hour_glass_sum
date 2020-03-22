#!/bin/python3
# https://www.hackerrank.com/challenges/2d-array/problem

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            """
            arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
            arr[0][1]+arr[0][2]+arr[0][3]+arr[1][2]+arr[2][1]+arr[2][2]+arr[2][3]
            arr[0][2]+arr[0][3]+arr[0][4]+arr[1][3]+arr[2][2]+arr[2][3]+arr[2][4]
            arr[0][3]+arr[0][4]+arr[0][5]+arr[1][4]+arr[2][3]+arr[2][4]+arr[2][5]

            arr[1][0]+arr[1][1]+arr[1][2]+arr[2][1]+arr[3][0]+arr[3][1]+arr[3][2]
            ...
            ..
            arr[1][3]+arr[1][4]+arr[1][5]+arr[2][4]+arr[3][3]+arr[3][4]+arr[3][5]
            ###

            arr[3][3]+arr[3][4]+arr[3][5]+arr[4][4]+arr[5][3]+arr[5][4]+arr[5][5]
            """
            if col > 3 or row > 3:
                break
            hour_glass_sum = (
                arr[row][col]
                + arr[row][col + 1]
                + arr[row][col + 2]
                + arr[row + 1][col + 1]
                + arr[row + 2][col]
                + arr[row + 2][col + 1]
                + arr[row + 2][col + 2]
            )
            if col == 0 and row == 0:  # initial condition
                max_hour_glass_sum = hour_glass_sum
            max_hour_glass_sum = max(max_hour_glass_sum, hour_glass_sum)
    return max_hour_glass_sum


if __name__ == "__main__":

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    result = hourglassSum(arr)
    print(result)
