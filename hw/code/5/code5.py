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






























