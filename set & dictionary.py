#set{}

basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)
{'pear','banana','apple','orange'}

'orange' in basket
True
'crabgrass' in basket
False

a = set('abracadabra') 				
b = set('alacazam')
a 					# unique letters in a
a - b 				# letters in a but not in b
a | b 				# letters in a or b or both
a & b 				# letters in both a and b
a ^ b 				# letters in a or b but not b

a = {x for x in 'abracadabra' if x not in 'abc'}
a
a = {x for x in 'abracadabra' if x in 'abc'}
a


if x in 'abc'
 for x in 'abracadabra'
 print(x)

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.add("watermelon")
fruits
fruits.update("grape")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits


>>>Dictionaries

#Another useful data type built into python is the dictionary

tel = {'jack': 4098, 'scpe': 4139}
tel['jack']
tel['guido'] = 4127
tel
del tel['scpe']
tel
tel ['irv'] = 4127
tel
list(tel)

'guido' in tel
'scpe' not in tel

dict([('scpe', 4139), ('guido', 4127), ('jack', 4098)])
dict(scpe=4139, guido=4127, jack=4098)
dict(4139, 4127, 4098)

{x: x**2 for x in (2,4,6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}


#when looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k,v)

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'Yangon': 'Myanmar'}
for k, v, z in knights.items():
	print(k, v, z)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for x, y in knights.items():
	print(x, y)