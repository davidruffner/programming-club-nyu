#!/usr/bin/python

# Open a file

def readInput(filename):
  """
  Copied from Mark Hannel's Crypt.py code

  NAME: readInput

  PURPOSE: reads in a text file with the format
  given by the UVA output description.

  INPUT: filename as a string

  OUTPUT: A list containing the number of words
  in the dictionary, the words of the dictionary,
  several encrypted lines which need to be decrypted.
  """
  #Check for proper input
  if type(filename) != str:
      print 'Filename must be a string!'
      return -1

  f = open(filename, 'r')

  #Create list container for necessary elements
  result = []
  result.append(int(f.readline()))
  for line in f.readlines():
      result.append(line.rstrip('\n'))

  #Close file
  f.close()

  return result

def match(word1,word2):
  '''Copied from Mark Hannel's Crypt.py'''
  for i,j in zip(word1,word2):
    if   i == j: pass
    elif j == '*': pass 
    else: return False
  
  return True

