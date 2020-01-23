#Loops
Loops.py

-While Loops
-for Loops

Condition is ture, while loop exeute a set of statements

x = 1
while x < 7:
	print(x)
	x +=1

1
2
3
4
5
6

while loop require variable ready.

x = 1
while x < 7:
	print(x)
	if x == 5:
			break
		x += 1

1
2
3
4
5

for Loops

# loops is iterating over a sequence

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
		print(x)

#Looping in a String
for x in "pineapple"
	print(x)

#The break Statement

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
		print(x)
		if x == "pineapple"
			break

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
		if x == "pineapple"
			break
		print(x)


# The continue Statement - stop the current interation

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
		if x == "pineapple":
			continue
		print(x)

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
		if x == "banana" amd x == "coconut":
			continue
		print(x)



# The range() Function - a set of code a specified number of times

for x in range(10):
		print(x)

for x in range(10,100):
	print(x)

jack 5(jump)

for x in range(10,100,5): 
	print(x)


#Nested loops

NumberA = [1,2,3,4,5]
NumberB = [1,2.3,4,5]
for x in NumberA:
	for y in NumberB:
		print(x,y)

NumberA = [1,2,3,4,5]
NumberB = [1,2.3,4,5]
for x in [1,2,3,4,5]
	for y in [1,2,3,4,5]
		print(x,y)

NumberA = [1,2,3,4,5]
NumberB = [1,2.3,4,5]
for x in NumberA:
		for y in NumberB:
			for z in [1,2,3,4,5]:
				print(x,y,z)


#Pass

for x in [1,2,3,4,5]
	pass

words = ['cat', 'window', 'defenestrate']
for w in words:
		print(w, len(w))

for n in range(2,10):
	for x in range(2,n):
			if n%x == 0:
				print(n, 'equals', x, '*', n//x)
				break
	else:
					# loop fell through without finding a factor
					print(n, "is a prime number")


2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 euals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3


for num in range (2,10):
	if num % 2 == 0:
		print("Found an even number",num)
		continue
	print("found a number", num)


found a even number 2
found a number 3
found a even number 4
found a number 5
found a even number 6
found a number 7
found a even number 8
found a number 9


for num in range (2,10):
	if num % 2 == 0:
		print("Found an even number",num)
		break
	print("found a number", num)

found a number 2






