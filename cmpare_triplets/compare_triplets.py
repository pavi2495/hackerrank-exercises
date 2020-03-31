#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.

def compareTriplets(a, b):
    count = 0
    count1 = 0
    al = len(a)
    for i in range(al):
        if a[i] > b[i]:
            count += 1
        elif a[i] < b[i]:
            count1 += 1
    return (count ,count1)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT'], 'w')

    a = list(map(int, input().rstrip().split()))


    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()