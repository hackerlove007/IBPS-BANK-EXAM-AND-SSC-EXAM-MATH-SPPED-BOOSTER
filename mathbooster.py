while 1:
	import random
	num1 = random.randint(0,1000)
	num2 = random.randint(99,1000)
	print(num1,num2 ,"both numbers are added")
	ans = int(input("enter your calculated number:"))
	realans = num1 * num2
	if ans == num1 * num2:
	    print("you are right and correct answer is" ,realans )
	else:
	    print("u r wrong and real answer is", realans)
