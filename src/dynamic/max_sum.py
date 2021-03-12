#!/bin/python3
import time

'''
  Given an array of n integers,
  find the subset of non-adjacent elements with the maximum sum
  :param arr: The money in hand.
  :type arr: list<int>
  :return: The maximum sum that can be obtained from a non-adjacent subset
  :rtype: int
'''

def maxSubsetSum(arr):
  dp = {} # key : max index of subarray, value = sum
  dp[0], dp[1] = arr[0], max(arr[0], arr[1])
  print(dp)
  for i, num in enumerate(arr[2:], start=2):
      dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
      print(dp)
  return dp[len(arr)-1]
  # max_sum = 0
  # for i in range(0, len(arr)):
  #   for j in range(2, len(arr), 1):
  #     local_combos = [[arr[i]]]
  #     for k in range(i + j, len(arr), 2):
  #       # print('k', k)
  #       combo_copy = [row[:] for row in local_combos]
  #       for x in combo_copy:
  #         new_comb = x + [arr[k]]
  #         if(new_comb not in local_combos):
  #           local_combos.append(new_comb)
  #     max_local = max(sum(l) for l in local_combos)
  #     max_sum = max_local if max_local > max_sum else max_sum
  # return max_sum

# n_num = int(input("Please enter the no. of integers:").rstrip())
# arr = []
# for _ in range(n_num):
#   arr.append(int(input("Please enter integer no. {} :".format(_ + 1)).rstrip()))

arr = [1,2,3,4,5]
# arr = [3, 7, 4, 6, 5]
# arr = [2, 1, 5, 8, 4]
# arr = [3, 5, -7, 8, 10]

start = time.process_time()
print("The maximum sum that can be obtained from a non-adjacent subset is: {}".format(maxSubsetSum(arr)))
print("{} ms".format((time.process_time() - start) * 1000))