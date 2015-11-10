total_bill = float(raw_input("What is your total bill?"))
tip_percent = float (raw_input("How much do you want to tip?"))
num_friends = float (raw_input("How many friends are you with?"))
tip = tip_percent/100.0

def tips_with_friends(total_bill):
	should_tip= (total_bill * tip)/num_friends
	return should_tip

print "Each person should pay:", "%.2f" % tips_with_friends(42.50)




#print "%f" % calculate_tip(42.50)

