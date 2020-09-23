#!/bin/python3

def removeNonIntersections(str_left, str_right):
  str_left_list = list(str_left)
  str_right_list = list(str_right)
  intersections = []
  for value in str_left_list:
    if value in str_right_list:
      intersections.append(value)
      str_right_list.remove(value)

  return ((len(str_left) - len(intersections)) + (len(str_right) - len(intersections)))


str_left = input("Please enter String 1:")
str_right = input("Please enter String 2:")
print("Number of characters to remove to make string 1 and string 2 as anagrams of each other: {}".format(removeNonIntersections(str_left, str_right)))




