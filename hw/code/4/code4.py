import random


def getRandomState():
	x = randrange(-10000,10000) 
	return x 



def startSimAnn:
	s0 = getRandomState();
	e0 = getEnergyAtState(s0);
	s,e=s0,e0
	sb,eb=s,e
	k = 0

	while k < kmax and e > emax:
		sn = neighbor(s)
		en = getEnergyAtState(sn)

		if (en < eb):
			sb,eb = sn,en
			print "!"

		if ( en < e ):
			s,e = sn,en
			print "+"
		else:
			if probOfAccept(e,en,k/kmax) < rand():
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
