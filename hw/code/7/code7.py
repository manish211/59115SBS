from model import *
import math
import random


def lo(curr_candidate_sol,d):
	return curr_candidate_sol.lowerRange[d]


def hi(curr_candidate_sol,d):
	return curr_candidate_sol.upperRange[d]


def decisions(curr_candidate_sol):
	return [_ for _ in xrange(curr_candidate_sol.numOfDec)]


def trim(x,d):
	return max(lo(d), min(x,hi(d)))

def score(thingObj,model):
	temp_obj = model()
	temp_obj.decisionVec = thingObj.have
	f1,f2 = temp_obj.getobj()
	square = lambda val: math.pow(val,2)
	sq_root = lambda val: math.sqrt(val)
	dist_from_hell =sq_root(square(f1) + square(f2))
	return dist_from_hell 



def candidate(model):
	curr_candidate_sol = model()
	something = [lo(d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d)) for d in decisions(curr_candidate_sol)]
	new = Thing()
	new.have = something
	new.score = score(new,model)
	return new


def de(model, max = 100, f = 0.75, cf = 0.3, epsilon = 0.01):
	info_model_candidate = model()
	np = info_model_candidate.numOfDec * 10
	frontier = [candidate(model) for _ in xrange(np)]
	for k in xrange(max):
		total,n = update(f,cf,frontier)
		if total/n > (1 - epsilon):
			break
	for x in frontier:
		print x
	return frontier

def update(f,cf, frontier, total=0.0, n=0):
	for x in frontier:
		s = x.score
		new = extrapolate(frontier,x,f,cf)
		if new.score > s:
			x.score = new.score
			x.have = new.have
		total +=x.score
		n += 1
	return total,n

def extrapolate(frontier, one, f, cf):
	out = Thing(id = one.id, have = copy(one.have))
	two, three, four = threeOthers(frontier, one)
	changed = False
	numOfDecisions = len(out.have)
	for d in range(numOfDecisions):
		x,y,z = two.have[d], three.have[d], four.have[d]
		if random.random() < cf:
			changed = True
			new = x + f*(y-z)
			out.have[d] = trim(new,d)
	if not changed:
		d = a([d for d in range(numOfDecisions)])
		out.have[d] = two[d]
	out.score = score(out)
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


if __name__ == "main":
	print "Starting Differential Evolution. Hold on tight."
	print "================================================"
	model=Golinski
	de(model)



























