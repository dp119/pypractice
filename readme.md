
# <h1> Python Topics

# <h4> Python Language and Python Implementations


# <h4> Python Compiler and Portability


# <h4> Dynamic Language (like Javascript and Ruby)

	* Variable Declaration

	
# <h4> Type Annotation or Type Hinting



# <h4> Mutable and Immutable variables

	* Int is Immutable
	
	* Lists are mutable
	

	
	
# <h4> String Operations

	
	course = "Python Programming"

	print(len(course)) 			#prints lenght of string

	print(course[0:3])			#returns "Pyt"

	print(course[:3])			#returns "Pyt"

	print(course[0:])			#returns "Python Programming"

	print(course[:])			#returns "Python Programming"

	print(course[-1]) 			#returns "g"

	
# <h4> Escape Sequences

	
	message = "Python \"Programming\" "

	message = "Python\'s Programming"

	message = "Python \\Programming"

	message = "Python \nProgramming"



# <h4> Useful String Methods

	
	course = " Python Programming"
	
	print(course.upper())
	
	print(course.lower())
	
	print(course.title())
	
	print(course.strip())
	
	print(course.find("Pro"))		#find index of the character
									#string comparison's are case sensitive
									
	print(course.replace("P", "-"))
	
	print("Programming" in course)	#returns boolean True
	
	print("Programming" not in course)	#returns boolean False
	
	
# <h4> Numbers

Binary representation of the numbers
	
	
	x = 10
	print(bin()x))		#prints binary representation of number 10
	
	x = 0x12c
	print(x)			#prints number decimal representation of the hexadecimal value
	
	print(hex(x))		#prints hexadecimal representation of given number
	
	

Arithmetic Operations
	
	
	x = 10 + 3
	x = 10 - 3
	x = 10 * 3
	x = 10 / 3		#returns float
	x = 10 // 3		#returns integer
	x = 10 % 3		#modulus returns remainder
	x = 10 ** 3		#power 
	

Augmented assignment operator	
	
	
	x = x + 1
	x += 1
	
	

There are no incremental operators unlike Java (x++ or x--)
	
	
# <h4> Working with Numbers

	*
	import math
	PI = 3.14		#by convention upper case variables are used for constants. Although this value can be changed, it's just a convention. Because there are no constants in python
	print(round(PI))
	print(abs(PI))
	
:exclamation: *Complete list of python built in functions available [here](https://docs.python.org/3/library/functions.html/)* 

	
:exclamation: *Complete list of methods in math module available [here](https://docs.python.org/3/library/math.html/)*

	
# <h4> Type Conversion

	
	input("x: ")
	y = x + 1 		#Returns type conversion error
	
Python is strongly typed language. It does not perform explicit type conversion
Javascript is weakly typed language. It does perform implicit type conversions
	
	
	
	print(int(x))		# 1
	print(float(x))		# 1.0
	print(bool(x))		# True
	print(str(x))		# 1
	
	
Truthy and Falsy Boolean Values.
Any of the below values, if we try to convert to boolean, the result will be false. Everything else is true

	
	bool(0)				# returns false
	bool("")			# returns false
	bool([])			# returns false
	bool(None)			# returns false
	bool("false")		# returns true
	
	
# <h4> Conditional Statements


		age = 22
		if age >= 18:
		  print("Adult")
		elif age >= 13:
		  print("Teenager")
		else:
		  print("child")
		  
		print("All done")
		


		if x > 1:
			pass	#use pass keyword to have an empty block
		else:
			pass
			
			
# <h4> Logical Operators


Eg for "not" operator: To find if given string is empty. If uses the concept of Falsy boolean

	name = " "
		
	if not name.strip():        #use strip to remove empty spaces
		print("Name is empty")
	else:
		print("Name is not empty")

Eg for "and" operator

	age = 22
	if age >= 18 and age <= 65:
		print("Eligible")

We could re-write above like below as well and eliminate "and"

	if 18 <= age < 65:
		print("Eligible")
		
# <h4> Ternary Operators

	message = "Eligible" if age >= 18 else "Not Eligible"
	
# <h4> Loops

For Loops
	for x in "Python":
		print(x)
		
	for x in ['a','b','c']:
		print(x)
		
	for x in range(5):
		print(x)
		
	for x in range(0, 10, 2):
		print(x)				#prints 0 2 4 6 8
		
		
Difference between list and range objects
	
# <h4> For..Else


	names = ["John", "Mary"]
	for name in names:
		if name.startswith("J"):
			print("Found")
			break
	else:
		print("Not found")	
	

# <h4> While Loops

	guess = 0
	answer = 5

	while answer =! guess:
		guess = int(input("Guess: "))
	else:
		pass


# <h4> Functions

Difference between lists and tuple

What is PEP 8
PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code

What is keyword argument



#Function returns single value

	def increment(number, by):
		return number + by


	print(increment(2, 3))

#return multiple value

	def incrementby(number, by):
		return (number, number + by)  # returns a tuple (which is read only unlike lists)


	print(incrementby(2, 3))


#keyword argument
	print(increment(2, by=3))


#function with default value
	def increment(number, by=1):
		return (number, number + by)

	print(increment(2))


#Type hinting / type annotation in functions
	def increment(number: int, by: int =1) -> tuple:
		return (number, number + by)


		
# <h5> *Learn more about markdown [here](https://guides.github.com/features/mastering-markdown/)*