import random
import math
import sys

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

	constraints = [0,0,0,0,0,0]

	constraints[0] = candidate[0] + candidate[1] - 2

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

	objs = [0,0]  # Empty list of size 2

	objs[0] = -(25*square(candidate[0] - 2) + square(candidate[1] -2)
		+ square(candidate[2] - 1)*square(candidate[3] - 4)
		+ square(candidate[4] - 1))

	objs[1] = square(candidate[0]) + square(candidate[1])+square(candidate[2]) + square(candidate[3])+square(candidate[4]) + square(candidate[5])

	return objs


def gen_rand_candidates():
	candidate = [0,0,0,0,0,0]
	candidate[0] = random.randrange(0,10)
	candidate[1] = random.randrange(0,10)
	candidate[2] = random.randrange(1,5)
	candidate[4] = random.randrange(1,5)
	candidate[3] = random.randrange(0,6)
	candidate[5] = random.randrange(0,10)

	return candidate


def get_valid_rand_candidates():
	while True:
		candidate = gen_rand_candidates()
		if((constraint_checker(candidate)) and (var_bound_checker(candidate))):
			return candidate

def randomize_no_greed(solution,c):
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


def get_start_end(solution,c,steps):
	if((c == 0) or (c == 1) or (c == 5)):
		start = 0
		end = 10

	if((c == 2) or (c == 4)):
		start = 1
		end = 5

	if(c == 3):
		start = 0
		end = 6

	return (start,end)


def randomize_with_greed(solution,c,min,max):
	best_score = 0
	best_solution = [0,0,0,0,0,0]
	steps = 1000
	start,end = get_start_end(solution,c,steps);

	step_size = float(end - start)/steps	
	for x in xrange(1,steps):
		# print "start=",start," end=",end, " step_size=", step_size, " value of X=", x
		# solution=randomize_no_greed(solution,c)    # Do this in steps
		solution[c] = start + x*step_size
		# print "solution[c]:=", solution[c], " value of C=", c
		raw_score_solution = raw_score(solution)
		score_solution = raw_score_solution/(max-min)
		if (constraint_checker(solution)) and (score_solution > best_score):
			best_score = score_solution
			best_solution = solution[:]


	return best_solution

def raw_score(solution):
	objs = get_objectives(solution)
	raw_sum = objs[0] + objs[1]
	return raw_sum

def getMinMax():
	min_score = 999999999
	max_score = -999999999
	
	for x in xrange(1,1000):
		candidate = get_valid_rand_candidates()
		raw_sum = raw_score(candidate)
		if raw_sum > max_score:
			max_score = raw_sum
		if raw_sum < min_score:
			min_score = raw_sum

	return (min_score,max_score)


def flush():
	sys.stdout.flush()


def run_max_walk_sat(max_tries,max_changes,epsilon, prob):
	best_score=0 #for maximization
	best_solution=[0,0,0,0,0,0]
	is_sol_found=False

	# Compute min, max only once and use it for getting score
	min,max = getMinMax()  #Get min max first for baselining

	# print "min:", min
	# print "max:", max

	if min < 0:
		min = 0

	counter = 0
	for i in xrange(1,max_tries):
		solution = get_valid_rand_candidates()

		for j in xrange(1,max_changes):
			raw_score_solution = raw_score(solution)
			if raw_score_solution > max:
				max = raw_score_solution      #Get the new max if current score is better than max : Changing the boundaries

			score_solution = raw_score_solution/(max-min)  #Normalize	

			if (score_solution > 0) and ((epsilon - score_solution) > 0 and (epsilon - score_solution) < 0.005):
				print "Got solution ...exiting"
				print "score_solution:", score_solution
				print "epsilon - score_solution=", (epsilon - score_solution)
				is_sol_found = True
				best_score = score_solution
				break
			#Just for logging the best solution so far		
			if score_solution > best_score:
				best_score = score_solution
				best_solution = solution[:]

			c = random.randint(0,(len(solution) - 1))  #c is a random index picked up from 0 to length of solution list

			if prob < random.random():
				solution = randomize_no_greed(solution,c)
				counter1 = 0
				while(constraint_checker(solution) and counter1 <=1000):
					if(counter1%100 == 0):
						print "$",
						counter += 1
						flush()
					solution = randomize_no_greed(solution,c)
					counter1 += 1
				print "?",
				counter += 1
			else:
				solution = randomize_with_greed(solution,c,min,max)
				counter2 =0;
				# print " ---------"
				if (constraint_checker(solution)):
					print "+",
					counter += 1
				else:
					print ".",
					counter += 1
			
		if counter%50 == 0:
			print ""
			flush()
		
		print "\n",i,":=================="

		if is_sol_found == True:
			break

	
	print "========================================"
	print "MAXWALK ALGORITHM RESULT SUMMARY"
	print "========================================"
	print "BEST SOLUTION FOUND:= ", best_solution
	print "BEST SCORE FOUND:=", best_score
	print "REQUESTED THRESHOLD:=", epsilon
	print "REQUESTED APPROX. ERROR:=", 0.005
	return ("failure", best_solution, best_score)



if __name__ == "__main__":
	print "Starting Max Walk Sat Algorithm : Hold on tight!"
	print "Notations: ? means global search\n + means local search\n $,^ are constraint checks performed in global and local search respectively\n"
	print "====================OBSERVE OUTPUT BELOW========================="
	epsilon = 0.689
	max_tries = 1000
	max_changes = 200
	prob = 0.5
	run_max_walk_sat(max_tries, max_changes, epsilon, prob)
































