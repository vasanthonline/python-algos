#!/bin/python3
import time

'''
  To accept an integer n and find the fibonacci value at index n.
  :param n: The input interger n.
  :type n: int
  :return: The fibonacci value at index n.
  :rtype: int
'''
def fibonacci(n):
  if(n == 1):
    return 1
  if(n == 0):
    return 0
  return fibonacci(n - 1) + fibonacci(n - 2)  
# n = input("Please enter an integer:")

n = 16

start = time.process_time()
print("The fibonacci value at {} is : {}".format(n, fibonacci(n)))
print("{} ms".format((time.process_time() - start) * 1000))