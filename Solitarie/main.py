#!/usr/bin/python

import pygame
from pygame.locals import *
from sys import exit

def main():
  CONS_MOUSEBTN = 1
  running = True
  imgBoard = '/home/sivious/Dropbox/Cosas/Programacion/git-python/Solitarie/textures/board.png'

  
  try:
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600),0, 24)
    
    # Fill background
    background = pygame.image.load(imgBoard)
    background = background.convert()

    # Display some text
    
    #text = font.render("Hello There", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    loadNewGame(screen)
    
    # Event loop
    while running:
      #event = pygame.event.get()
      #con el de abajo funciona
      event = pygame.event.wait()

      if event.type == pygame.QUIT:
        running = False
      #elif event.type == pygame.MOUSEMOTION:
      #  print "Mouse at (%d, %d)" %event.pos
      elif event.type == pygame.MOUSEBUTTONDOWN and event.button == CONS_MOUSEBTN:
        #print event.pos
        whichBall(event.pos)
      
  finally:
    pygame.quit()

def loadNewGame(screen):
  mGame = [['P', 'P', 'O', 'O', 'O', 'P', 'P'],
  ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'F', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['P', 'P', 'O', 'O', 'O', 'P', 'P'],
  ['P', 'P', 'O', 'O', 'O', 'P', 'P']]

  startPosX = 201
  startPosY = 101
  ballIter = 60

  imgRedBall = '/home/sivious/Dropbox/Cosas/Programacion/git-python/Solitarie/textures/redBall.png'

  for rows in mGame:
    for item in rows: 
      if item == 'O':
        b = pygame.sprite.Sprite() # create sprite
        b.image = pygame.image.load(imgRedBall).convert() # load ball image
        b.rect = b.image.get_rect() # use image extent values
        b.use_alpha = True
        b.rect.topleft = [startPosX, startPosY] # put the ball in the top left corner
        screen.blit(b.image, b.rect)
        #redBall = pygame.image.load(imgRedBall)
        #redBall = redBall.convert_alpha()
        #screen.blit(redBall, (startPosX, startPosY))
      startPosX += ballIter
    startPosY += ballIter
    startPosX = 201
  pygame.display.flip()

  
def whichBall(posList):
  x = int(posList[0])
  y = int(posList[1])

  print "X: " + str(x) + " Y: " + str(y)

if __name__ == '__main__':
  main()
