from datetime import datetime, timedelta
from sys import stdout
from time import sleep
 
print ("Cronometro regressivo | programador => mmxm")
segundos = float(input("Digite a quantidade de segundos: "))
tempo = timedelta(seconds=segundos)
print ("\n")
 
while (str(tempo) != '0:00:00'):
	stdout.write("\r%s\n"%tempo)
	stdout.flush()
	tempo = tempo - timedelta(seconds=1)
	sleep(1)
 
stdout.write("\r0:00:00")
stdout.flush()

print ("\a")
