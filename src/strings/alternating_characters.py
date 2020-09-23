#!/bin/python3

# To take a string as an input, iterate thro each char and remove char which are sequentially repetitive.
# Return the length of the non-repetitive string.

def removeAlternatingChars(string):
  seq = list(string)
  tmp = seq[0]
  for item in seq[1:]:
    def checkDupl(tmp, item):
      if tmp[-1] == item:
        return tmp
      return tmp + item
    tmp = checkDupl(tmp, item)
  return len(string) - len(tmp)


string = input("Please enter a String:")

print("Number of characters to remove to make the string with non-repeating characters: {}".format(removeAlternatingChars(string)))