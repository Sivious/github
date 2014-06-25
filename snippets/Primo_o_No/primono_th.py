#import thread
import time
from threading import Thread

def div_rec(num, numini, numfin, result, index):
	numit = numfin
	result[index] = True

	while (result[index] and numit > numini):
		#print numit
		if num % numit == 0:
			result[index] = False
		numit -= 2
		

if __name__ == '__main__':
	start_time = time.time()
	primo = True
	
	threads = [None] * 10
	results = [None] * 10
    
	num = int(raw_input("Introduce numero: "))
	numeval = num
    
	if num % 2 == 0:
		primo = False
	else:
		numeval = num - 2
		for i in range(len(threads)):
			threads[i] = Thread(target=div_rec, args=(num, 1, numeval, results, i))
			threads[i].start()
		
		#primo = div_rec(num, 1, numeval)
		
		for i in range(len(threads)):
			threads[i].join()
			
	for i in range(len(results)):
		if results[i] == False:
			primo = False
	
	if primo:
		print "El numero es primo"
	elif not primo:
		print "El numero no es primo"
	
	print time.time() - start_time, "seconds"
	
	print "\nFIN"  