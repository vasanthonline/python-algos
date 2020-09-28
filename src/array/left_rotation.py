#!/bin/python3

'''
  To take an array of digits and perform 'd' left rotations on the array
  Return the array after all the rotations are complete.
  :param arr: The input array
  :type arr: list
  :return: The array after all the rotations are complete.
  :rtype: list
'''
def leftRotation(arr, rotations):
  if(rotations == 0 or len(arr) == 0):
    return arr 

  if(rotations > len(arr)):
    rotations = rotations % len(arr)
  return arr[rotations:] + arr[:rotations]
  
arr = list(map(int, list(input("Please enter the array of digits:").rstrip())))
rotations = int(input("Please enter the no. of rotations:").rstrip())

print("The array after {} rotations: {}".format(rotations, leftRotation(arr, rotations)))