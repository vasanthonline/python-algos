#!/bin/python3
import time

'''
  To take two strings and check whether there is a common substring
  :param str_left: The input string no. 1
  :param str_right: The input string no. 2
  :type str_left: str
  :type str_right: str
  :return: YES if there is a common string. NO if there is no such substring
  :rtype: str
'''
def stringMatch(str_left, str_right):
  match = False
  for i in str_left:
    if(i in str_right):
      match = True
      break
  return 'Yes' if match else 'No'
  
  
# str_left = input("Please enter String 1:")
# str_right = input("Please enter String 2:")

str_left = "hello"
str_right = "world"

start = time.process_time()
print("Is there a common substring between string 1 and string 2: {}".format(stringMatch(str_left, str_right)))
print("{} ms".format((time.process_time() - start) * 1000))