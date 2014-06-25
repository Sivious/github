import os
import sys

#sys.argv[1] = "D:\"

# os.listdir(sys.argv[1])

print sys.argv[1]


	for item in os.listdir(sys.argv[1]) :
		if os.path.isdir(item) :
			print item + "is a dir"
		elif os.path.isfile(item) :
			print item + "is file"
        

