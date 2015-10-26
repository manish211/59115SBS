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
	else
		return False
	