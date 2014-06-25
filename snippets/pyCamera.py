import pygame
import pygame.camera
from pygame.locals import *
import time

#delay de 5 minutos para hacer una foto cada 5 minutos
iDelay = 60 * 5
#el for se va a realizar durante 3 horas
iIterator = 36

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()

for i in iIterator :
  image = cam.get_image()
  pygame.image.save(image, "/home/sivious/Descargas/screen" + str(i) +".jpg")

cam.stop()

