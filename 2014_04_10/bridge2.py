#!/usr/bin/python

'''
Solution to Bridge problem
David Ruffner
Begin Time: 1:29pm
End Time: 

 REFERENCE: algorithm based on paper by Gunter Rote,
        "Crossing the Bridge at Night", http://page.mi.fu-berlin.de/rote/Papers/pdf/Crossing+the+bridge+at+night.pdf

  Plan is to find the number of tag team steps analytically
'''
from time import sleep
import numpy as np
import sys
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

  '''could be a better way of doing it:>with open(filename,'r') as f:'''
  #Create list container for necessary elements
  result = []
  result.append(int(f.readline()))
  for line in f.readlines():
      result.append(line.rstrip('\n'))

  #Close file
  f.close()

  return result

def totaltimes(npeople,times):
    """
  NAME: totaltimes

  PURPOSE: Calculates the total time required to cross bridge for all
           the possible numbers,k, of times using the tag-team strategy

  INPUT: number of people and the sorted times of each person to cross bridge
            as an array

  OUTPUT: A list containing the total time required for everyone to cross
          the bridge for each value of k

  REFERENCE: algorithm based on paper by Gunter Rote. You can think about it
             by seeing how the time changes by doing one more tag team step
  """
    kmax = int(np.floor((npeople-1)/2.))
    Tks = np.zeros(kmax+1)
    Tks[0] = (npeople-2)*times[0]+np.sum(times[1:])
    for k in np.arange(kmax)+1:
        Tks[k] = 2*times[1] - times[0] - times[npeople-2*k] + Tks[k-1]
    return Tks

def tagteamstep(k,npeople,times):
    '''Send fast people ahead, then send a pair of slow people'''
    #print out this part of the schedule
    print times[0],times[1]
    print times[0]
    print times[npeople-1],times[npeople-2]
    print times[1]
    #decrement the values to account for people crossing bridge
    newtimes = times[:-2]
    newk = k-1
    newnpeople = npeople-2
    return [newk,newnpeople,newtimes]

def ferrystep(k,npeople,times):
    '''use fast people to ferry the slow across'''
    #print out this part of the schedule
    print times[0],times[-1]
    print times[0]
    print times[0],times[-2]
    print times[0]
    #decrement the values to account for people crossing bridge
    newtimes = times[:-2]
    newk = k-1
    newnpeople = npeople-2
    return [newk,newnpeople,newtimes]

def bridge2(filename):
    #Check for proper input
    if type(filename) != str:
        print 'Filename must be a string!'
        return -1
    problem = readInput(filename)
    
    ncases = int(problem.pop(0))
    for i in np.arange(ncases):
        problem.pop(0)
        npeople = int(problem.pop(0))
        
        #extract the times and clean up
        times = problem[0:npeople]
        times = [int(time) for time in times]
        times.sort()
        times = np.array(times)
        del problem[0:npeople]

        #Calculate the total time to cross bridge
        Tks = totaltimes(npeople,times)
        print Tks
        print int(np.min(Tks)) #print the minumum time to cross

        #Find k value with the minimum Tks
        k = np.argmin(Tks)#Do tagteam step k times

        #Build the schedule
        while npeople >= 4:
            if k > 0:
                out = tagteamstep(k,npeople,times)
            else:
                out = ferrystep(k,npeople,times)
            [k, npeople ,times] = out
        if npeople == 3:
            print times[0],times[2]
            print times[0]
            print times[0],times[1]
        else:
            print times[0],times[1]
        
        print ''


if __name__ == '__main__':
  bridge(sys.argv[1])
