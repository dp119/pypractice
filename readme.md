
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

	*
	course = "Python Programming"

	print(len(course)) 			#prints lenght of string

	print(course[0:3])			#returns "Pyt"

	print(course[:3])			#returns "Pyt"

	print(course[0:])			#returns "Python Programming"

	print(course[:])			#returns "Python Programming"

	print(course[-1]) 			#returns "g"

	
# <h4> Escape Sequences

	*
	message = "Python \"Programming\" "

	message = "Python\'s Programming"

	message = "Python \\Programming"

	message = "Python \nProgramming"



# <h4> Useful String Methods

	*
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

	*
	Binary representation of the numbers
	x = 10
	print(bin()x))		#prints binary representation of number 10
	
	x = 0x12c
	print(x)			#prints number decimal representation of the hexadecimal value
	
	print(hex(x))		#prints hexadecimal representation of given number
	
	


	*
	Arithmetic Operations
	x = 10 + 3
	x = 10 - 3
	x = 10 * 3
	x = 10 / 3		#returns float
	x = 10 // 3		#returns integer
	x = 10 % 3		#modulus returns remainder
	x = 10 ** 3		#power 
	
	
	*
	Augmented assignment operator
	x = x + 1
	x += 1
	
	
	*
	There are no incremental operators unlike Java (x++ or x--)
	
	
# <h4> Working with Numbers

	*
	import math
	PI = 3.14		#by convention upper case variables are used for constants. Although this value can be changed, it's just a convention. Because there are no constants in python
	print(round(PI))
	print(abs(PI))
	
	Complete list of python built in functions [here](https://docs.python.org/3/library/functions.html) 
	
	Complete list of methods in math module [here](https://docs.python.org/3/library/math.html)
	
	
	
	
# <h5> *Learn more about markdown [here](https://guides.github.com/features/mastering-markdown/)*