If_Else_Statement.py

#Boolean Expersion

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


python Conditions

Equals					->		x==y
Not Equals				->		x!=y
Less than				->		x<y
Less than or Equals		->		x<=y
Greater than			->		x>y
Greater than or equal to	->	x>=y
Boolean or              ->      x or y ,x | y
Boolean AND				->		x and y,x & y
Boolean Not             ->      not X


if-
else-

#if Statement

x = 70
y = 60
if x >y:
	print("x is greater than y")


elif -- else if
x = 70
y = 60
if x < y:
	print("x is greater than y")
else:
	print("x is not greater than y")



x = 70
y = 60
if x < y:
	print("x is greater than y")
elif x == y:
	print("x is equal to y")
else:
	print("x is not greater than y")



x = 70
y = 60
if x < y:
	print("x is greater than y")
elif x == y:
	print("x is equal to y")
elif x > y:
	print("x is greater than y")
else:
	print("x is not greater than y")


x = 70
y = 60
if x < y:
	print("x is greater than y")
elif x == y:
	print("x is equal to y")
elif x > y:
	print("x is greater than y")
elif x != y:
	print("x is not equal y")
elif y < x:
	print("y is smaller than x")
else:
	print("x is not greater than y")



x = 70
y = 60
if x < y:
	print("x is greater than y")
elif x == y:
	print("x is equal to y")
elif x != y:
	print("x is not equal y")
elif x > y:
	print("x is greater than y")
elif y < x:
	print("y is smaller than x")
else:
	print("x is not greater than y")


#Short Hand If

if x > y: print("x is greater than y")


# Elif

x = 70
y = 70
if x >y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")

#Else
x = 50
y = 150
if x > y:
	print("x is greater than y")
elif
	print("x and y are equal")
else:
	print("x is less than y")



# Short Hand If ... ELse
x = 50
y = 150
print(x) if x > y else print(y)

#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
		print("All conditions are True")


#Or si logical operator

x = 50
y = 40
z = 100
if x > y or z >y:
	print("one of the conditions is Ture")
elif x > y and z > y:
	print("All conditions are True")
else:
	print("nothing else")



if x > y and z < y or x < y:
	print("Line No 1 is True")
elif x < z or y < z or z == y:
	print("LIne No 2 is Ture")
elif z > y and x > y and x != y:
	print("Line No 3 is Ture")
else:
	print("Nothing Ture")


#Nested If is if Statements in if statements

x = 50
if x > 10:
	print("x is ten")
if x > 20:
	print("x is greater than 20")
else:
	print("No,x is not greater than 20")


x = 5
if x > 10:
	print("x is ten")
if x > 20:
	print("x is greater than 20")
else:
	print("No,x is not greater than 20")
elif x < 10:
	print("x is small")
if x < 5:
	print("x is small than 5")
else:
	print("No,x is nothing")
else:
	print("x is bigger")


#Pass Statement

x = 100
y = 50

if x > y:
	pass


if x > y:
	print("x is greater than 10 and 20")
	pass
	print("x is not greater than 10 & 20")


x = int(input("Examination Results:"))

if x > 100 and x < 100 and x >= 90:
	print("Grade A")
elif x > 89 and x < 89 and x >= 70:
	print("Grade B")
elif x > 40 and x < 40 and z >= 40:
	print("Grade C")
elif 









