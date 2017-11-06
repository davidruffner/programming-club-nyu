'''
Solution to Crypt Kicker
Mark Hannel
Begin Time: 4:45 pm
End Time:  6:15 pm
'''

from time import sleep
import sys

def readInput(filename):
  """
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


def lencheck(word1,word2):
  if len(word1) == len(word2):
    return True
  else: 
    return False

def match(word1,word2):
  for i,j in zip(word1,word2):
    if   i == j: pass
    elif j == '*': pass 
    else: return False
  
  return True

def decryptWord(word,cipher):
  currWord = ''
  for letter in word:
    try:
      currWord = currWord.__add__(cipher[letter])
    except KeyError:
      currWord = currWord.__add__('*')
  return currWord

def compareDict(word,diction):
  possWords = []
  for possWord in diction:
    if match(possWord,word):
      possWords.append(possWord)
  return possWords

def decryptRecurse(words, ordDict,  number, cipher):
  """
  NAME: decyptRecurse

  PURPOSE: Given a set of words and a list of words nested 
  by word length, attempt to create a consistent cipher that 
  deciphers the text. If unsuccessful, returns -1.  Should 
  only be called within decrypt because there is no attempt 
  to check input format

  INPUT:
  words - list of words which are to be decrypted.  The first
  "number" of the words have been used to make the cipher, the
  remaining words are to be tested for consistency.  The
  number+1 word will be used to add to the cipher
  ordDict - A list of lists with the nth list containing
  all words of length n
  number - An integer giving the index of the first word 
  we should use to add to cipher
  cipher - a python dictionary containing the proposed cipher key

  OUTPUT: a list containing the decrypted words (if successful)
  or the integer -1 (if fails)
  """
  '''
  decryptRecurse is assumed to have the correct input.
  currword is the word we will work on. We assert that
  currword will be correct and create a cipher.
  Using the cipher, we check the next word for
  inconsistency. If consistent, continue, else break.
  '''
  
  numWords = len(words)

  #Decipher word using cipher. If no match, place *
  currWord = decryptWord(words[number],cipher)
  
  #If word is deciphered, then theres nothing to add
  #to cipher. Go on to the next word
  lenWord = len(currWord)

  if ordDict[lenWord-1].__contains__(currWord):
    newWords = words
    newWords[number] = currWord
    return decryptRecurse(newWords,ordDict, number+1, cipher)

  #Find all possible words that could match.    
  possWords = compareDict(currWord,ordDict[lenWord-1])
                        
  for possWord in possWords:
    # Add to cipher
    newCipher = cipher.copy()
    for i,j in zip(possWord,words[number]):
      newCipher.update({j:i})
    
    # Check for injectivity... couldn't think of simpler phrase
    values = newCipher.values()
    if len(values) != len(set(values)):
        continue

    # Check if you're at the end
    if number+1  >= numWords:
      newWords = words
      newWords[number] = possWord
      return newWords

    # Continue to the next word if not at the end
    newWords = words
    newWords[number] = possWord
    test = decryptRecurse(newWords, ordDict, number+1, newCipher)
    if test != -1:
      return test
    else: pass
  else: pass

  #If no possible word works, then return -1
  return -1
  
def decrypt(filename):
  """
  NAME: decrypt

  PURPOSE: Given a dictionary of n words, attempt to succesfully
  decrypt several encrypted messages

  INPUT: problem - a list containing the output of
  readInput

  OUTPUT: Successfully or unsuccessfully decrypted messages
  """

  #Check for proper input
  if type(filename) != str:
      print 'Filename must be a string!'
      return -1

  problem = readInput(filename)
  
  #Collect words of dictionary and messages
  diction  = problem[1:problem[0]+1]
  messages = problem[problem[0]+1:]

  #Organize dictionary based on length of word
  longLen = 0
  for word in diction:
    wordLen = len(word)
    if wordLen>longLen:
      longLen = wordLen

  ordDict = [ [] for i in xrange(longLen)]

  for word in diction:
    wordLen = len(word)
    ordDict[wordLen-1].append(word)
  
  #File to write solution to
  filename = filename.rstrip('.txt')
  f = open(filename+'sol.txt','w')

  #Iterate over messages attempting to decrypt each.
  for message in messages:
    words = message.split()
    result = decryptRecurse(words, ordDict, 0, {})
    if result != -1:
      f.write(' '.join(result)+'\n')
    else:
      f.write(' '.join(['*'*len(word) for word in words])+'\n')

  return 1


if __name__ == '__main__':
  decrypt(sys.argv[1])
