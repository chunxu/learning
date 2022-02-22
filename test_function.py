# this is a script to test whether a function works

# define a function to add numbers
def add_num (a,b):
	return a+b

# ask for inputs 
a = input ("please input a number: ")
b = input ("please input another number:")

# turn inputs into numbers
try:
	a = float (a)
except:
	print("Your 1st input is not a number.")
try:
	b = float (b)
except:
	print("Your 2nd input is not a number.")

# output sum
if type(a) == float and type(b) == float:
	print ("the sum of your inputs are {}".format(add_num(a,b)))
else:
	print("Cannot be operated due to input err.")


