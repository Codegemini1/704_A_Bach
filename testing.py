def even_odd(a):
	if a % 2 == 0:
		print('Even Number')
	else:
		print('Odd Number')

def int_filter(*args):
	for i in args:
		if type(i) == int:
			print(i)