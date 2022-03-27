import time
from class_tracks import step


x = True  #va varier avec start/stop (penser a remettre le compteur a zero avec start)

last_step = 0
current_step = 1
tempo_lenght = 1 #TEMPO
a=0 #compteur track A
b=0 #compteur track B

def count() :
	while x == True :
		now = time.monotonic()
		last_time = 0
		if now - last_time >= tempo_lenght :
			print(stepMatrix[1][current_step].gateOn)
			last_time = now
			last_step = current_step
			current_step += 1
			playStep(last_step)
			a += 1
			b += 1
			for i in range(2):
				if stepMatrix[0][a].rst == 1:
					a = 0
				if stepMatrix[1][b].rst == 1:
					b = 0
			if current_step > 7 :
				current_step = 0
				print("I did reset, fuck, it feels good")
		
				
				
def playStep (value) :
	for i in range(2) :
		while now - last_time < stepMatrix[i][current_step].len :
			#digitalOut(i) = stepMatrix[i][current_step].gateOn
			print(stepMatrix[i][current_step].gateOn)
		
		