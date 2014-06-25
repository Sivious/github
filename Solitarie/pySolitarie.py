#!/usr/bin/env python

import os

#define constants
pOccupied = 'O'
pFree = 'F'
pProhibited = 'P'

mGame = [
['P', 'P', 'O', 'O', 'O', 'P', 'P'],
['P', 'P', 'O', 'O', 'O', 'P', 'P'],
['O', 'O', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'F', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', 'O', 'O'],
['P', 'P', 'O', 'O', 'O', 'P', 'P'],
['P', 'P', 'O', 'O', 'O', 'P', 'P']]

#Cleaning function

class cls(object):
  def __repr__(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    return ''

#This function simply print the (in) Matrix
def printBoard(mBoard = []):
  numRow = 0
  print '  0123456'
  for rows in mBoard:
    board = ''
    for item in rows: 
      if item == 'P': board += ' '
      elif item == 'O': board += 'X'
      elif item == 'F': board += ' '
    print str(numRow) + ' ' + board
    numRow += 1
    
#this function consolidate the board with the correct move

def moveIt (posFrom = [], posTo = []):
  posFromX = int(posFrom[0])
  posFromY = int(posFrom[1])
  posToX = int(posTo[0])
  posToY = int(posTo[1])
  
  mGame[posFromX][posFromY] = 'F'
  mGame[(posFromX+posToX)//2][(posFromY+posToY)//2] = 'F'
  mGame[posToX][posToY] = 'O'

#this function returns if a tab can move to the position 
def canMove(posFrom = [], posTo = []):
  posFromX = int(posFrom[0])
  posFromY = int(posFrom[1])

  posToX = int(posTo[0])
  posToY = int(posTo[1])
  
  mMoves = []

  # Create a list with the 4 possible movements
  # using the ternary operators (op1 if condition else op2)
  if mGame[(posFromX+posToX)//2][(posFromY+posToY)//2] == 'O' :
    mMoves.append([posFromX-2 , posFromY, mGame[posFromX - 2][posFromY]] if posFromX-2 >= 0 else 'P') 
    mMoves.append([posFromX , posFromY-2, mGame[posFromX][posFromY - 2]] if posFromY-2 >= 0 else 'P') 
    mMoves.append([posFromX+2 , posFromY, mGame[posFromX + 2][posFromY]] if posFromX+2 <= 5 else 'P') 
    mMoves.append([posFromX , posFromY+2, mGame[posFromX][posFromY + 2]] if posFromY+2 <= 5 else 'P') 
  
  if [posToX, posToY, pFree] in mMoves:
    return True
  else:  
    return False

def newGame ():
  mGame = [['P', 'P', 'O', 'O', 'O', 'P', 'P'],
  ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'F', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
  ['P', 'P', 'O', 'O', 'O', 'P', 'P']]
  
print 'Game Start'
newGame()
printBoard(mGame)

while 1 == 1:
  selection = raw_input('Play>> ')
  token = selection.split(' ')

  if token[0] == 'move' and len(token) == 3 :
    try:
      porFrom = []
      posFrom = token[1].split(',', 1)
      posTo = []
      posTo = token[2].split(',', 1)
    
      if canMove(posFrom, posTo) :
        moveIt(posFrom, posTo)
        printBoard(mGame)
      else :
        print 'Movement not allowed!'
    except ValueError:
        print 'Bad Spelling!'
  elif token[0] == 'print' :
    printBoard(mGame)
  elif token[0] == 'quit' :
    print 'Bye' 
    break
  elif token[0] == 'printBoard' :
    print mGame
  elif token[0] == 'help' :
    print 'Commands:'
    print '  move [POSITION SOURCE] [POSITION DESTINATION]'
    print '    Example: move 1,3 3,3'
    print '  print'
    print '  printBoard (DEVELOPER COMMAND)'
    print '  help'
    print '  help'
    print '  newGame'
  elif token[0] == 'newGame' :
    newGame()
    printBoard(mGame)
  else:
    print 'Incorrect command' 


