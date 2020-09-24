#!/bin/python3

'''
  To take a string as an input, check for two conditions:
  1. Do the string has all characters appear the same number of times?
  2. By removing just 1 character at a single index, does the condition #1 satisfy?
  If either of these condition satisfy, consider the string as valid.
  :param string: The input string
  :type str: string
  :return: Whether the string satifies one of the two conditions or not.
  :rtype: boolean
'''
def isValidString(string):
  seq = list(string)
  dictionary = {}
  for item in seq:
    def countChar(tmp, item):
      if item in tmp:
        tmp[item] = tmp[item] + 1
      else:
        tmp[item] = 1
      return tmp
    dictionary = countChar(dictionary, item)

  dict_values_list = list(dictionary.values())
  dict_values_unique_list = list(set(dict_values_list))
  not_list = [item for item in dict_values_list if item != dict_values_list[0]]
  in_list = [item for item in dict_values_list if item == dict_values_list[0]]
  
  if(len(dict_values_unique_list) == 1):
    return 'YES'
  elif(len(dict_values_unique_list) == 2 and len(not_list) == 1):
    if(not_list[0] - 1 == in_list[0]):
      return 'YES'
    elif(not_list[0] - 1 == 0):
      return 'YES'
  elif(len(dict_values_unique_list) == 2 and len(in_list) == 1):
    if(in_list[0] - 1 == not_list[0]):
      return 'YES'
    elif(in_list[0] - 1 == 0):
      return 'YES'

  return 'NO'

string = input("Please enter a input String:")
print("Does the string have all characters appear the same number of times: {}".format(isValidString(string)))