
response = "S"

while (response == "S" or response == "s"):

	num = int(raw_input("Introduce numero: "))
	
	addi = num // 10
	
	rang1 = 1
	rang2 = addi +1
	
	for i in range(10):
		print "[" + str(rang1) + ":" + str(rang2) + "]"
		rang1 = rang2
		rang2 = rang1 + addi
	
	response = str(raw_input("Desea repetir (S)/(N): "))
	
