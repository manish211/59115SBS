from model import *


def lo(curr_candidate_sol,d):
	return curr_candidate_sol.lowerRange[d]


def hi(curr_candidate_sol,d):
	return curr_candidate_sol.upperRange[d]


def decisions(curr_candidate_sol):
	return [_ for _ in xrange(curr_candidate_sol.numOfDec)]


def trim(x,d):
	return max(lo(d), min(x,hi(d)))


def candidate(model):
	curr_candidate_sol = model()
	something = [lo(d) + n(hi(curr_candidate_sol,d) - lo(curr_candidate_sol,d)) for d in decisions(curr_candidate_sol)]
	new = Thing()
	new.have = something
	new.score = score(new)
	return new


def de(model, max = 100, f = 0.75, cf = 0.3, epsilon = 0.01):
	info_model_candidate = model()
	np = info_model_candidate.numOfDec * 10
	frontier = [candidate(model) for _ in xrange(np)]
	for k in xrange(max):
		total,n = update(f,cf,frontier)
		if total/n > (1 - epsilon):
			break
	return frontier

