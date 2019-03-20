
import sys
while True:
	print("1.Triangle\n2.Square\n3.Pyramid\n4.Diamond\n5.Exit")
	ch = int(input("Please enter your choice : "))

	def triangle():
		n = int(input("Enter the value : "))
		for i in range(1,n+1):
			for j in range(1,i+1):
				print("*",end=" ")
			print("")

	def square():
		n = int(input("Enter the value : "))
		for i in range(1,n+1):
			for j in range(1,n+1):
				print("*",end=" ")
			print("")

	def pyramid():
		n = int(input("Enter the value : "))
		for i in range(1,n+1):
			print((n-i)*" "+(i*"* "))

	def diamond():
		n = int(input("Enter the value : "))
		for i in range(1,n+1):
			print((n-i)*" "+(i*"* "))
		for i in range(1,n+1):
			print((i*" ")+(n-i)*"* ")
	def exit():
		sys.exit()		
	dict = {
			1:triangle,
			2:square,
			3:pyramid,
			4:diamond,
			5:exit
			}
	dict.get(ch)()