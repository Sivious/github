import thread

def div_rec(num, numini, numfin):
	numit = numfin
	esPrimo = True

	while (esPrimo and numit > numini):
		if num % numit == 0:
			esPrimo = False
		numit -= 2
	return esPrimo
	
if __name__ == '__main__':
	primo = True
    
	num = int(raw_input("\nIntroduce numero: "))
	numeval = num
    
	if num % 2 == 0:
		primo = False
	else:
		numeval = num - 2
		primo = div_rec(num, 1, numeval)
	
	if primo:
		print "\nEl numero es primo"
	elif not primo:
		print "\nEl numero no es primo"

	print "\nFIN"  