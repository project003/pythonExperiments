

previous_number = 0
next_number = 1
value = int(input("Enter how many terms for fabonacci series : "))
print(next_number,end=" ")
for i in range(value-1):
	number = previous_number+next_number
	print(number,end = " ")
	previous_number=next_number
	next_number=number


  
