SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
	"""Convert a file size to human_readable form.
	keyword arguments:
	size -- file size in bytes

	Returns: string
	"""
	multiple = 1024
	for suffix in SUFFIXES:
		size /= multiple
		if size < multiple:
			return f'{size} {suffix}' #sarebbe il format

	raise ValueError('number too large') #genera eccezione