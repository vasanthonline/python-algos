#!/bin/python3
import time

'''
  To take an input of n indicating the no. of stairs in the house and 
  assuming that the stairs can be climbed 1, 2 or 3 steps at a time,
  find the no. of ways the stair case could be climbed.
  :param n: The input interger n.
  :type n: int
  :return: The no. of ways the staircase could be climbed.
  :rtype: int
'''
cache = dict()

def stepPerms(n):
  if n == 1:return 1
  if n == 2:return 2
  if n == 3:return 4
  if n not in cache:
      cache[n] = stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
  return cache[n]


# n = input("Please enter an integer:")
n = 5

start = time.process_time()
print("The no. of ways a {} step stair case could be climbed : {}".format(n, stepPerms(n)))
print("{} ms".format((time.process_time() - start) * 1000))