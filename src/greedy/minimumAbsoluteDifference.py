#!/bin/python3

import re

'''
  Given an array of integers, find and print the minimum absolute difference between any two elements in the array
  :param arr: The list of integers
  :type arr: list
  :return: The minimum difference between any two elements in the array
  :rtype: int
'''

def minimumAbsoluteDifference(arr):
  minDifference = float('inf')
  arr.sort()
  for i in range(0, len(arr) - 1):
    diff = abs(arr[i] - arr[i + 1])
    if(diff < minDifference):
      minDifference = diff
  return minDifference

# string = input("Please input a list of integers separted by space:")
# arr = list(map(int, string.split()))
arr = [1, -3, 71, 68, 17]
print("is valid: {}".format(minimumAbsoluteDifference(arr)))