import random
import math

def  var_bound_checker(candidate = []):
	true_count = 0

	if(0 <= candidate[0]) and (candidate[0] <= 10):
		true_count += 1;

	if(0 <= candidate[1]) and (candidate[1] <= 10):
		true_count += 1;
	
	if(1 <= candidate[2]) and (candidate[2] <= 5):
		true_count += 1;
	
	if(1 <= candidate[4]) and (candidate[5] <= 5):
		true_count += 1;

	if(0 <= candidate[3]) and (candidate[3] <= 6):
		true_count += 1;

	if(0 <= candidate[5]) and (candidate[5] <= 10):
		true_count += 1;

	if( true_count == 6):
		return True
	else:
		return False


def constraint_checker(candidate = []):
	true_count = 0

	make_square = lambda x: math.pow(x,2)

	make_cube = lambda x: math.pow(x,3)

	constraints = []

	constraints[0] = candidate[0] + candidate[1] -2

	constraints[1] = 6 - candidate[0] - candidate[1]

	constraints[2] = 2 - candidate[1] + candidate[0]

	constraints[3] = 2 - candidate[0] + 3*candidate[1]

	constraints[4] = 4 - make_square(candidate[2] - 3) - candidate[3]

	constraints[5] = make_cube(candidate[4] - 3) + candidate[5] - 4

	if (( 0 <= constraints[0] ) and ( 0 <= constraints[1] ) 
	and ( 0 <= constraints[2] ) and ( 0 <= constraints[3] )
	and ( 0 <= constraints[4] ) and ( 0 <= constraints[5] )):
		return True
	else:
		return False


def get_objectives(candidate=[]):
	square = lambda x:math.pow(x,2)

	objs = []

	objs[0] = -(25*square(candidate[0] - 2) + square(candidate[1] -2)
		+ square(candidate[2] - 1)*square(candidate[3] - 4)
		+ square(candidate[4] - 1))

	objs[1] = square(candidate[0]) + square(candidate[1])+square(candidate[2]) + square(candidate[3])+square(candidate[4]) + square(candidate[5])

	return objs


def gen_rand_candidates():
	candidate[0] = random.randrange(0,10)
	candidate[1] = random.randrange(0,10)
	candidate[2] = random.randrange(1,5)
	candidate[4] = random.randrange(1,5)
	candidate[3] = random.randrange(0,6)
	candidate[5] = random.randrange(0,10)

	return candidate


def get_valid_rand_candidates():
	while True:
		candidate = gen_rand_candidates
		if((constraint_checker(candidate)) and (var_bound_checker(candidate))):
			return candidate

def randomize_no_greed(solution=[],c):
	if(c == 0):
		solution[0] = random.randrange(0,10)

	if(c == 1):
		solution[1] = random.randrange(0,10)

	if(c == 2):
		solution[2] = random.randrange(1,5)

	if(c == 4):
		solution[4] = random.randrange(1,5)

	if(c == 3):
		solution[3] = random.randrange(0,6)

	if(c == 5):
		solution[5] = random.randrange(0,10)

	return solution



def randomize_with_greed(solution=[],c,min,max):
	best_score = 0
	best_solution = []

	for x in xrange(1,1000):
		solution=randomize_no_greed(solution,c)
		score_solution = score(solution,min,max)
		if(score_solution > best_score):
			best_score = score_solution
			best_solution = solution[:]

	return best_solution

def score(solution=[],min,max):
	objs = get_objectives(solution)
	raw_sum = objs[0] + objs[1]
	normalized_sum = raw_sum/ (max - min)
	return normalized_sum

def getMinMax():
	min_score = 999999999
	max_score = -999999999
	
	for x in xrange(1,9999999):
		candidate = get_valid_rand_candidates()
		objs = get_objectives(candidate)
		raw_sum = objs[0] + objs[1]	
		if raw_sum > max_score:
			max_score = raw_sum
		if raw_sum < min_score:
			min_score = raw_score

	return (min_score,max_score)



def run_max_walk_sat(max_tries,max_changes,epsilon, prob):
	best_score=0 #for maximization
	best_solution=[]

	# Compute min, max only once and use it for getting score
	# multiple times. This removes unnecessary duplication of
	# heavy computation
	min,max = getMinMax()  #Get min max first for baselining


	for i in xrange(1,max_tries):
		solution = get_valid_rand_candidates()

		for j in xrange(1,max_changes):
			score_solution = score(solution,min,max)
			if score_solution > epsilon:
				return "success",solution

		#Just for logging the best solution seen so far
		if score_solution > best_score:
			best_score = score_solution
			best_solution=solution[:]

		c = random.choice(solution)

		if prob < random():
			solution = randomize_no_greed(solution,c)
			print "?"
		else:
			solution = randomize_with_greed(solution,c)
			print "!"

	return "failure", best_solution, best_score



if __name__ == "__main__":
	print "Starting Max Walk Sat Algorithm : Hold on tight!"
	epsilon = 0.00000001
	max_tries = 100000
	max_changes = 2000
	prob = 0.5
	run_max_walk_sat(max_tries, max_changes, epsilon, prob)































