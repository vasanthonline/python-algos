#!/bin/python3

'''
  To take a 6x6 array and find the sum of each hour glass from the array. 
  Return the maximum sum of the sums from the hour glasses.
  :param arr: The input 2-dimensional 6x6 array
  :type arr: 6x6 array
  :return: The maximum sum of the sums from the hour glasses.
  :rtype: int
'''
def hourGlassSum(arr):
  sums = []
  for i in range(0, len(arr)):
    sub = arr[i]
    for j in range(0, len(sub)):
      if(j+2 < len(sub) and i+2 < len(arr)):
        sums.append(sub[j] + sub[j+1] + sub[j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    
  return max(sums)

arr = []
arr = [[-9,-9,-9,1,1,1],
[0,-9,0,4,3,2],
[-9,-9,-9,1,2,3],
[0,0,8,6,6,0],
[0,0,0,-2,0,0],
[0,0,1,2,4,0]]
# arr = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 0], [6, 7, 8, 9, 0, 1]]
# for _ in range(6):
#   arr.append(list(map(int, list(input("Please enter the {} row of 6 digits:".format(_ + 1)).rstrip()))))

print("Maximum sum of hour glass for the array is: {}".format(hourGlassSum(arr)))