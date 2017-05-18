# Bridget Wright
# Student No: 10354568
# B8IT105 Programming for Big Data
# CA5b - Calculator, Python, Lambda, Map, Filter, Reduce
# A calculator that can handle lists of data


# Lambda, Map, Reduce, Filter, List Comprehension, Generator

# Code from tutorial in class
add = lambda x,y : x+y
print add(1,1)

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print F

C = map(celsius, F)
print C

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]
print map (lambda x,y:x+y, a,b)
print map(lambda x,y,z:x+y+z, a,b,c)
print map(lambda x,y,z:x+y-z, a,b,c)

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result

print reduce(lambda x, y: x+y, [47, 11, 42, 13])

f = lambda a,b: a if (a>b) else b
print reduce(f, [47, 11, 42, 13]) 


# Functions using reduce
def max (values):
	return reduce (lambda a,b: a if (a>b) else b, values)	
print max([47, 11, 42, 13]) 
	
def min (values):
	return reduce (lambda a,b: a if (a<b) else b, values)	
print min([47, 11, 42, 13]) 

def add (values):
	return reduce (lambda a,b: a if (a+b) else b, values)
print add([47, 11, 42, 13]) 

# Functions using filter
def is_even (values):
	return filter (lambda x: x % 2 == 0, values)
print is_even([47, 11, 42, 13]) 


def is_odd (values):
	return filter (lambda x: x % 2, values)
print is_odd([47, 11, 42, 13]) 


# Functions using reduce
def divide (values):
	return reduce (lambda a,b: a/float(b) if (b != 0 and a != 'Nan') 
		else 'Nan', values)
print divide([47, 11, 0, 42, 13, 0]) 
print divide([47, 11, 42, 13, 0]) 
print divide([47, 11, 42, 13]) 

def multiply (values):
	return reduce (lambda a,b: a*b, values)
print multiply([47, 11, 42, 13, 0]) 

# Functions using map
def to_fahrenheit (values):
	return map (fahrenheit, values)
print to_fahrenheit ([0, 37, 40, 100])
	
def to_celcius (values):
	return map (celcius, values)
print to_fahrenheit ([0, 32, 100, 212])

def sum(to):
	return reduce (lambda x, y: x+y, range (1, to+1))
print sum(100)


# Function using list comprehension
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Fahrenheit

# Pythagorean triples 
#### note here the use of 2 indents - Python recognises that 2 lines are on the 1 line
print [(x,y,z) for x in range(1,30) for y in range(x,30) 
		for z in range(y,30) if x**2 + y**2 == z**2]



# Product of two sets
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things


# Name Generators
def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

x = city_generator()
print x.next()

print x.next()

print x.next()

print x.next()

# print x.next()


# this code is not in tutorial
cities = city_generator()
for city in cities:
	print city

	
### don't forget n in the first line!
def get_triplets(n):
	for x in range (1,n):
		for y in range (x,n):
			for z in range (y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)
					
triplets = get_triplets(30)
for triplet in triplets:
	print triplet,

# Function with yield statement
### Fibonacci - create a generator that will go up to the 5th Fibonacci sequece
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(50)
for x in f:
    print x,
print






















