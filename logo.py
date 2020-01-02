#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All conditions are True")

#Or is logical operator

x = 50 
y = 40
z = 100
if x > y or x > y:
	print ("one of the conditions is True")

#filested If is statements in if statements

x = 50

if x > 10:
	print ("x is ten")
	if x > 20:
		print ("x is greater than 20")
	else:
		print("No,x is not greater than 20")