#!/bin/python3

import re

'''
  To take a string as an input and validate it for alphanumberic characters based on paranthesis.
  :param string: The input string
  :type string: str
  :return: Validity of the string.
  :rtype: boolean
'''
def validate(string):
  return re.replace('(', '').replace(')', '').isalnum()

def isValid(string):
  braces = []
  isValid = True
  for s in string:
    if(s != '(' and s != ')'):
      continue
    if(s == '('):
      braces.append(s)
    elif(s == ')'):
      if(len(braces) > 0):
        braces.pop()
      else:
        isValid = False
        break
  if(len(braces) != 0):
    isValid = False
  return isValid

  



# string = input("Please enter a String:")
string = "a(b(c(de))(fgh)"
# string = "(a)(b)(c)(d)(de(rF)ed)"
print("is valid: {}".format(isValid(string)))