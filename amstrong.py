import sys

def amstrong(n):
	'''function for calculting sum ''' 
	sum = 0  #initializing sum
	temp = n
	while temp>0:
		digit = temp%10
		sum = sum + digit ** 3
		temp //= 10  
	return sum

class main:
	'''Class for providing options to user'''
	while True: 
		choice = int(input("1.Check amstrong number\n2.EXIT\n"))
		if choice == 1:
			number=int(input("Enter the number : "))	
			sum = amstrong(number)
			if sum == number: 					#validating whether sum and number is same or not
				print("\nThis is amstrong number")
			else:
				print("\nThis is not an amstrong number")
		elif choice == 2:  						#For exit program
			print("Thank you ....")
			sys.exit()
		else:
			print("\nPlease enter valid choice ")

			
	
  
