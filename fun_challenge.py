value = 5

def do_twice(f,value):
	f()
	value

def print_spam():
	print 'spam'

do_twice(print_spam,value)