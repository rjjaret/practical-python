

def timethis(func):
	from time import time
	
	def wrapper(*args, **kwargs):
		start=time()
		r = func(*args,**kwargs)
		end=time()
		print ('%s.%s: %f' % (func.__module__, func.__name__, end-start))
		
	return wrapper