#!/usr/bin/python

'''
Solution to Erdos
David Ruffner
Begin Time: 9:53am
            11:02am

            1:44pm
            3:32
End Time:  
'''
from time import sleep
import numpy
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
    

def erdos(filename):
    #Check for proper input
    if type(filename) != str:
        print 'Filename must be a string!'
        return -1
    problem = readInput(filename)
    #print problem

    #Get scenario number
    scenario = problem.pop(0)
    print "scenario "+str(scenario)

    #Get number of papers and number of names
    pn = problem.pop(0).split()
    p = pn[1]
    n = pn[0]
    
    #Get connections from the list of papers
    papers = problem[0:int(p)+1]
    #print papers
    papers = [(paper.split(':'))[0] for paper in papers]
    #print papers

    listpapernames = []
    allnames = []
    for paper in papers:
        papernames = paper.split(',') #Slices name list in paper
        odd = papernames[:-1:2]       #However we need to put initials
        even = papernames[1::2]       #with the respective name
        papernames = [i+','+j for i,j in zip(odd,even)]
        papernames = [name.strip() for name in papernames]
        #print papernames
        listpapernames.append(papernames)
        allnames = allnames+papernames
    #print listpapernames
    #print allnames

    uniqnames = set(allnames)
    #print uniqnames

    #Make a dictionary of contacts
    graph = {}
    for name in uniqnames:
        graph.update({name:[]})

    for papernames in listpapernames:
        for i in numpy.arange(len(papernames)):
            name = papernames.pop(i)
            connections = graph[name]
            connections = connections+papernames
            graph.update({name:connections})
            papernames.insert(i,name)
    # print "updated graph",graph
    # print "space"
    # for name in uniqnames:
    #     print name+": ", graph[name]

    #Starting at Erdos build up erdos numbers for the graph
    erdosnum = {}
    for name in uniqnames: #First initialize all to zero
        erdosnum.update({name:-1})
    
    erdos = 'Erdos, P.'
    erdosnum.update({erdos:0})

    todo = [erdos]
    while len(todo) > 0:
        node = todo.pop(0)
        nodenum = erdosnum[node]
        #print node
        neighbors = graph[node]
        for neighbor in neighbors:
            if erdosnum[neighbor]==-1:
                erdosnum.update({neighbor:nodenum+1})
                todo.append(neighbor)
                
    #print out erdos numbers
    testnames = problem[int(p)+1:]
    for name in testnames:
        num = erdosnum[name]
        if num == -1:
            num = 'infinity'
        print name, num

if __name__ == '__main__':
  erdos(sys.argv[1])
