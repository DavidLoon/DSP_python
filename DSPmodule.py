# function which standardizes list or array to zero mean and unit variance

import numpy as np
def standardize(x):

	try:	
		mean_x=np.mean(x)
		x=x-mean_x
		std_x=np.std(x)
		x=x/std_x
		return x
	except:
		print 'Error.'
		return False
