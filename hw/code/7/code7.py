from model import *
import math
import random


def lo(curr_candidate_sol,d):
	return curr_candidate_sol.lowerRange[d]


def hi(curr_candidate_sol,d):
	return curr_candidate_sol.upperRange[d]


def decisions(curr_candidate_sol):
	return [_ for _ in xrange(curr_candidate_sol.numOfDec)]


def trim(curr_candidate_sol,x,d):
	print "curr_candidate_sol:", curr_candidate_sol
	return max(lo(curr_candidate_sol,d), min(x,hi(curr_candidate_sol,d)))

def n(max):
	return int(random.uniform(0,max))

def score(curr_candidate_sol):
	f1,f2 = curr_candidate_sol.getobj()
	square = lambda val: math.pow(val,2)
	sq_root = lambda val: math.sqrt(val)
	dist_from_hell =sq_root(square(f1) + square(f2))
	return dist_from_hell


def get_min_max(model):
	min = 999999
	max = -999999
	for x in xrange(2000):
		temp_candidate_sol = model()
		temp_score = score(temp_candidate_sol)
		if(temp_score > max):
			max = temp_score
		if(temp_score < min):
			min = temp_score
	return (min,max)


class Thing():
	id = 0
	def __init__(self, **entries):
		self.id = Thing.id = Thing.id + 1
		self.__dict__.update(entries)

def candidate(curr_candidate_sol):
	curr_candidate_sol = model()
	curr_candidate_sol.decisionVec = [lo(curr_candidate_sol,d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d)) for d in decisions(curr_candidate_sol)]
	new = Thing()
	new.have = curr_candidate_sol.decisionVec
	new.score = score(curr_candidate_sol)
	return new


def de(model, baseline_min,baseline_max, max = 100, f = 0.75, cf = 0.3, epsilon = 0.01):
	curr_candidate_sol = model()
	print "FROM DE-->", curr_candidate_sol
	np = curr_candidate_sol.numOfDec * 10
	frontier = [candidate(curr_candidate_sol) for _ in xrange(np)]

	print "length of frontier:", len(frontier)

	for each_thing in frontier:
		if(each_thing.score < 0):
			baseline_min = 0
		if(each_thing.score < baseline_min):
			baseline_min = each_thing.score
		if(each_thing.score > baseline_max):
			baseline_max = each_thing.score



	#Normalize the scores of each thing now

	for each_thing in frontier:
		prev_each_thing_score = each_thing.score
		each_thing.score = float(each_thing.score - baseline_min)/(baseline_max - baseline_min)
		print "each_thing.id:", each_thing.id
		print "each_thing.score:", each_thing.score
		print "prev_each_thing_score:", prev_each_thing_score
	
	print "final baseline_max:", baseline_max
	print "final baseline_min:", baseline_min
	exit()
	
	for k in xrange(max):
		total,n = update(f,cf,frontier,curr_candidate_sol)
		if total/n > (1 - epsilon):
			break
	for x in frontier:
		print "print x:",x.id," ",x.have, x.score
	return frontier

def update(f,cf, frontier, curr_candidate_sol,total=0.0, n=0):
	print "FROM UPDATE -->", curr_candidate_sol
	for x in frontier:
		s = x.score
		curr_candidate_sol.decisionVec = x.have
		new = extrapolate(frontier,x,f,cf,curr_candidate_sol)
		if new.score > s:
			x.score = new.score
			x.have = new.have
		
		total +=x.score
		print "x.score:", x.score
		print "total:", total
		print "n:", n
		total +=x.score
		n += 1
	return total,n

def extrapolate(frontier, one, f, cf,curr_candidate_sol):
	print "FROM EXTRAPOLATE -->", curr_candidate_sol
	out = Thing(id = one.id, have = one.have[:])
	two, three, four = threeOthers(frontier, one)
	changed = False
	numOfDecisions = len(out.have)
	for d in range(numOfDecisions):
		x,y,z = two.have[d], three.have[d], four.have[d]
		if random.random() < cf:
			changed = True
			new = x + f*(y-z)
			out.have[d] = trim(curr_candidate_sol,new,d)
	if not changed:
		d = a([d for d in range(numOfDecisions)])
		out.have[d] = two.have[d]
		curr_candidate_sol.decisionVec = out.have
	out.score = score(curr_candidate_sol)
	return out


def threeOthers(lst, avoid):
	def oneOther():
		x = avoid
		while x.id in seen:
			x=a(lst)
		seen.append(x.id)
		return x

	seen = [ avoid.id ]
	this = oneOther()
	that = oneOther()
	theOtherThing = oneOther()
	return this, that, theOtherThing

def a(lst):
	return lst[n(len(lst))]


if __name__ == "__main__":
	print "Starting Differential Evolution. Hold on tight."
	print "================================================"
	model=Golinski
	baseline_min,baseline_max = get_min_max(model)
	print "baseline_min,baseline_max ", baseline_min," ",baseline_max
	de(model,baseline_min,baseline_max)

# if __name__ == "__main__":
# 	model=Golinski
# 	min,max = get_min_max(model)
# 	print "min,max ", min," ",max

























