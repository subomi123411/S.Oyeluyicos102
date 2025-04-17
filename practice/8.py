global x
x = 30

def inner_func():
	global x
	x = 50

def outer_func():
	global x
	inner_func()
	print("x in outer_func:", x)

outer_func()
print("x in global:", x)