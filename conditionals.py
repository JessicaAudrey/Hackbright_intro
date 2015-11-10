#your_name = "BEL"
#pairs_name = "BEN"
#if (your_name > pairs_name):
#	print "My name is greater:", your_name
#elif (your_name < pairs_name):
#	print "Their name is greater", pairs_name
#else:
	#print "our names are EQUAL"

#def compare_names(your_name, pairs_name):
#	if (your_name > pairs_name):
#		print "My name is greater:", your_name
#	elif (pairs_name < your_name):
#		print "Their name is greater", pairs_name
#	else:
#		print "our names are EQUAL"

#Todays_date = 4
#if (Todays_date > 15):
#	print "Oh, we're halfway there!"
#else: 
#	print "The month is still young"

#today = "Wed"
#if (today == "Monday"):
#	print "yay class day"
#elif (today == "tuesday"):
#	print "Its only Tuesday"
#elif (today == "Wed"):
#	print "HMPHDAY"
#elif (today == "thursday"):
#	print "#tbt"
#elif (today == "Friday"):
#	print "TTGIF"
#else:
#	print "weekend"

#age = float(raw_input("How old are you? "))
#def age_ok(age):
#	if (age >= float(21)):
#		print "Yay! I can go to a bar in the US..!"
#	elif (age >= float(18) and age < float(21)):
#		print "I can vote but I cannot go to a bar"
#	else:
#		print "Aww, I cannot vote or go to a bar."	

#age_ok(age)

#number = 8
#if (number %2 == 0):
	#print "The number 8 is even"
#else:
#	print "The number 8 is odd"
#
#if (number %2 == 1):
#	print "The number 8 is odd"
#else:
#	print "The number 8 is even"

number1 = 8
number2 = 9

#if (number1 %2 == 0 and number2 %2 == 0):
	#print "Both numbers are even."
#else:
	#print "Both numbers are not even."

if (number1 %2 == 0 and number2 %2 == 0):
	print "Both numbers are even."
elif (number1 %2 == 0 and number2 %2 ==1):
	print "8 is even and 9 is odd"
elif (number1 %2 == 1 and number2 %2 ==0):
	print "8 is odd and 9 is even"
else:
	print "Both numbers are odd"

favorite_color = raw_input("What is your favorite color? ")

if (favorite_color == "Blue" or favorite_color == "Yellow" or favorite_color == "Red"):
	print "My favorite color is a primary color!"
else:
	print "My favorite color is a secondary color."
