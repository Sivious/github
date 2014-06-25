#/usr/bin/python

import os

class Engine:
  def __init__(self):
    #define constants
    pOccupied = 'O'
    pFree = 'F'
    pProhibited = 'P'
    global mGame

    self.mGame = [
    ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
    ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'F', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
    ['P', 'P', 'O', 'O', 'O', 'P', 'P']]

  def __str__(self):
    viewBoard = " "
    for rows in self.mGame:
      for item in rows: 
        viewBoard += item
    
    return viewBoard

  def setmGame(self, mGame):
    self.mGame = mGame

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

engine = Engine()

print engine
