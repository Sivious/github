from PIL import Image
import sys
import os

if len(sys.argv) < 2:
    sys.stderr.write('Usage: sys.argv[0] \n')
    sys.exit(1)


if not os.path.exists(sys.argv[1]):
    sys.stderr.write('ERROR: image not found!\n')
    sys.exit(1)

fileName, fileExtension = os.path.splitext(sys.argv[1])
if fileExtension <> ".png" :
  sys.stderr.write('ERROR: Image must be png not ' + fileExtension +  '\n')
  sys.exit(1)

im = Image.open(sys.argv[1])
pix = im.load()

convImg = Image.new('RGBA', (im.size[0], im.size[1]), 'black')
convPix = convImg.load()


for w in range(0, im.size[0]) :
  for h in range(0, im.size[1]) :
    pixel = pix[w,h]  #Gets the RGBA code for the pixel
    convPix[w,h] = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2], pixel[3])

convImg.save("2_" + sys.argv[1])

print "END"
    
