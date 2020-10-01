#!/bin/python3
import time
from collections import Counter

'''
  To take a array fo size 'n' and a list of queries and perform for each query:
  Add a value to each of the array element between two given indices, inclusive.
  Return the maximum value of the manipulated array.
  :param arr: The input array
  :type arr: list
  :return: The array after all the rotations are complete.
  :rtype: list
'''
def manipulateArray(n, queries):
  c = Counter()
  for a,b,k in queries:
      c[a]  +=k
      c[b+1]-=k
  print(c)
  arrSum = 0
  maxSum = 0
  for i in sorted(c)[:-1]:
      arrSum+= c[i]
      maxSum = max(maxSum,arrSum)
  return maxSum

arr_size = int(input("Please enter the size of the array:").rstrip())
n_queries = int(input("Please enter the no. of queries:").rstrip())
queries = []
for _ in range(n_queries):
  queries.append(list(map(int, list(input("Please enter query no. {} :".format(_ + 1)).rstrip()))))

# arr_size = 40
# n_queries = 30
# queries = [[29,40,787],[9,26,219],[21,31,214],[8,22,719],[15,23,102],[11,24,83],[14,22,321],[5,22,300],[11,30,832],[5,25,29],[16,24,577],[3,10,905],[15,22,335],[29,35,254],[9,20,20],[33,34,351],[30,38,564],[11,31,969],[3,32,11],[29,35,267],[4,24,531],[1,38,892],[12,18,825],[25,32,99],[3,39,107],[12,37,131],[3,26,640],[8,39,483],[8,11,194],[12,37,502]]
# queries = [[2,3,603],[1,1,286],[4,4,882]]
start = time.process_time()
print("The maximum value in the array after {} queries: {}".format(n_queries, manipulateArray(arr_size, queries)))
print("{} ms".format((time.process_time() - start) * 1000))