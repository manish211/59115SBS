import random
import math

def getRandomState():
	x = random.randrange(-100000,100000) 
	return x

def neighbor():
	randomNeighbor = getRandomState()
	return randomNeighbor

def getEnergyAtState(x):
	# print x
	# print "------"	
	f1=pow(x,2)
	f2=pow((x-2),2)
	energy = f1 + f2
	if energy < 0:
		print "energy negative:",energy
		print "*****************************************"
		print "*****************************************"
	return energy 


def getMinMax():

	x=random.randrange(-100000,100000)	
	e=getEnergyAtState(x)

	minEnergy=e
	maxEnergy=e

	for i in range(100):
		x=random.randrange(-100000,100000)	
		
		e=getEnergyAtState(x)
	    	
		if(e<minEnergy):
			minEnergy = e

		if(e>maxEnergy):
			maxEnergy = e

	return minEnergy,maxEnergy


def getBaseLinedEnergy(x,minEnergy,maxEnergy):
	e=getEnergyAtState(x)
	# minEnergy,maxEnergy = getMinMax()
	baseLinedEnergyVal = float(e-minEnergy) / (maxEnergy - minEnergy)
	if baseLinedEnergyVal < 0:
		print "Energy is negative -----"
		print "======================================================"
		print "minEnergy:",minEnergy," maxEnergy:",maxEnergy," energy e:",e," baseLinedEnergyVal:",baseLinedEnergyVal
		print "======================================================"
	return baseLinedEnergyVal

def probOfAccept(old,new,temperature):
	probability = math.exp(float((old-new)/float(temperature)))
	return probability


def startSimAnn(emax):
	print "started"
	minEnergy,maxEnergy = getMinMax()
	s0 = getRandomState();
	e0 = getBaseLinedEnergy(s0,minEnergy,maxEnergy);
	s,e=s0,e0
	sb,eb=s,e
	k = 100
	kmax = k

	while k > 0 and e > emax:
		sn = neighbor()
		# print "Got the neighbor+++"
		# print sn
		# print "====="

		en = getBaseLinedEnergy(sn,minEnergy,maxEnergy)

		while en < 0:
			sn = neighbor()
			en = getBaseLinedEnergy(sn,minEnergy,maxEnergy)


		# print "Got the baseLinedEnergy++++"
		print "s,e:",s," ",e," ","sb,eb:",sb," ",eb," ""sn,en:",sn," ",en," "
		if (en < eb):
			sb,eb = sn,en
			print "!"

		if ( en < e ):
			s,e = sn,en
			print "+"
		else:
			# print "k:",;print k
			# print "kmax:",;print kmax
			temperature = float(k)/float(kmax)
			# print "current temperature:",
			# print temperature
			if probOfAccept(e,en,temperature) > random.random(): 
				s,e = sn,en
				print "?"

		print "."
		
		k = k - 1
		print "reduced k man:",
		print k," sb :",sb, " eb :",eb
		# if eb < 0:
		# 	print "+++++++++++++++++"
		# 	print "+++++++++++++++++"
		
		if k % 50 == 0:
			print "\n",sb
		
	return sb


if __name__ == "__main__":
	print "Starting Simulated Annealer : Hold on tight!"
	emax = 0.000000001
	startSimAnn(emax)
