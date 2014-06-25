if __name__ == '__main__':
    primo = True
    
    num = int(raw_input("\nIntroduce numero: "))
    numeval = num
    
    if num % 2 == 0:
        primo = False
    else:
        numeval = num - 2
        # print "Es primo: " + str(primo) + " ;Valor de numeval: " + str(numeval)
        while primo and numeval > 1:
            if num % numeval == 0:
                primo = False
            numeval -= 2
    
    if numeval == 1 and primo:
        print "\nEl numero es primo"
    elif not primo:
        print "\nEl numero no es primo"
    
    print "\nFIN"  