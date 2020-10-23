#!/bin/python3
import time
import itertools

'''
  To take an input of n indicating the no. of stairs in the house and 
  assuming that the stairs can be climbed 1, 2 or 3 steps at a time,
  find the no. of ways the stair case could be climbed.
  :param n: The input interger n.
  :type n: int
  :return: The no. of ways the staircase could be climbed.
  :rtype: int
'''

def fitChar(crwd, rowOrColNo, index, char, rowOrCol):
  (i, j) = (rowOrColNo, index) if rowOrCol == 'r' else (index, rowOrColNo)
  if(crwd[i][j] == '-' or crwd[i][j] == char):
    crwd[i][j] = char
    return crwd
  else:
    return False

def fitAOrientation(crwd, combs, rowOrColumn, fittedWords):
  for comb in combs:
    if(comb['word'] in fittedWords):
      continue
    fitment_copy = [row[:] for row in crwd]
    for i, r in enumerate(comb['range']):
      fitment_copy = fitChar(fitment_copy, comb['rowNo'], r, comb['word'][i], rowOrColumn)
      if(not fitment_copy):
        break
    if(fitment_copy):
      crwd = [row[:] for row in fitment_copy]
      fittedWords.append(comb['word'])
      if(len(fittedWords) == len(words)):
        break
    if(len(fittedWords) == len(words)):
      break
  return (crwd, fittedWords)

def fitACombo(crwd_copy, rowCombs, colCombs, fittedWord):
  fittedWords = [fittedWord]
  (crwd_copy, fittedWords) = fitAOrientation(crwd_copy, rowCombs, 'r', fittedWords)
  (crwd_copy, fittedWords) = fitAOrientation(crwd_copy, colCombs, 'c', fittedWords)
  
  if(len(fittedWords) == len(words)):
    return crwd_copy
  else:
    return False

def findCombos(crossword, words):
  fitment = []
  for word in words:
    def checkSeq(row, word):
      seq = []
      for i, ch in enumerate(row):
        if ch == '-' and len(seq) + 1 > len(word):
          seq = []
          break
        elif ch == '-' and (len(seq) == 0 or seq[-1] == i - 1):
          seq.append(i)
        elif ch != '-' and len(seq) == len(word):
          break
        else:
          seq = []

      return seq if len(seq) == len(word) else []

    applicable_rows = list(map(lambda row: checkSeq(row, word), crossword))
    for (index, row) in enumerate(applicable_rows):
      if(len(row) > 0):
        fit = dict()
        fit['rowNo'] = index
        fit['range'] = row
        fit['word'] = word
        fitment.append(fit)
  return fitment

def crosswordPuzzle(crossword, words):
  icrossword = [ [] for _ in range(len(crossword[0])) ]
  for i, row in enumerate(crossword):
    for col, char in enumerate(row):
      icrossword[col].append(char)

  rowCombs = findCombos(crossword, words)
  colCombs = findCombos(icrossword, words)

  crwd_copy  = []
  for rowComb in rowCombs:
    crwd_copy =  [row[:] for row in crossword]
    
    for i, r in enumerate(rowComb['range']):
      crwd_copy = fitChar(crwd_copy, rowComb['rowNo'], r, rowComb['word'][i], 'r')
    newRowCombs = [x for x in rowCombs if x['word'] != rowComb['word'] and (x['rowNo'] != rowComb['rowNo'] or x['range'] != rowComb['range'])]
    if(crwd_copy):
      crwd_copy = fitACombo(crwd_copy, newRowCombs, colCombs, rowComb['word'])
    if(crwd_copy):
      break
  
  if(crwd_copy):
    return crwd_copy

crossword = ['+-++++++++',
'+-++-+++++',
'+-------++',
'+-++-+++++',
'+-++-+++++',
'+-++-+++++',
'++++-+++++',
'++++-+++++',
'++++++++++',
'----------']
words = 'CALIFORNIA;NIGERIA;CANADA;TELAVIV'
words = words.split(';')

start = time.process_time()
crossword = list(map(lambda x: list(x), crossword))

print("The solved crossword puzzle : {}".format(crosswordPuzzle(crossword, words)))
print("{} ms".format((time.process_time() - start) * 1000))