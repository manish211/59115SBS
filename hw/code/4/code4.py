import random


def getRandomState():
	x = random.randrange(-10000,10000) 
	return x

def neighbor():
	return getRandomState

def getEnergyAtState(x):
	f1=pow(x,2)
	f2=pow((x-2),2)
	return f1+f2


def getMinMax():

	x=random.randrange(-10000,10000)	
	e=getEnergyAtState(x)

	minEnergy=e
	maxEnergy=e

	while i in range(100):
		x=random.randrange(-10000,10000)	
		
		e=getEnergyAtState(x)
	    	
		if(e<minEnergy):
			minEnergy = e

		if(e>maxEnergy):
			maxEnergy = e

	return minEnergy,maxEnergy


def getBaseLinedEnergy(x):
	e=getEnergyAtState(x)
	baseLinedEnergy = float(e-minEnergy) / (maxEnergy - minEnergy)
	return baseLinedEnergy

def probOfAccept(old,new,temperature):
	probability = pow(e,(old-new)/temperature)
	return probability


def startSimAnn:
	s0 = getRandomState();
	e0 = getBaseLinedEnergy(s0);
	s,e=s0,e0
	sb,eb=s,e
	k = 0

	while k < kmax and e > emax:
		sn = neighbor
		en = getBaseLinedEnergy(sn)

		if (en < eb):
			sb,eb = sn,en
			print "!"

		if ( en < e ):
			s,e = sn,en
			print "+"
		else:
			temperature = k/kmax
			if probOfAccept(e,en,temperature) < rand():
				s,e = sn,en
				print "?"

		print "."
		
		k = k + 1
		
		if k % 50 == 0:
			print "\n",sb
		
		return sb


if __name__ == "__main__":
	print "Starting Simulated Annealer : Hold on tight!"
	print "Best Solution is: "+startSimAnn
