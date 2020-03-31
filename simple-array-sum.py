#!/bin/python3

import os
import sys


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    count = 0
    ar_count = int(len(ar))
    for i in range(ar_count):

        if ar_count >= 0 and ar[i] <= 1000:
            count += ar[i]
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    print(f"{ar} hello ")
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

