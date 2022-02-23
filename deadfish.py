import sys


# main interpreter
def interpreter(code):
	accumulator = 0
	pointer = 0

	while pointer < len(code):
		instruction = code[pointer]
		
		# increase value of the accumulator by 1
		if instruction == "i":
			accumulator += 1
		# decrease value of the accumulator by 1
		elif instruction == "d":
			accumulator -= 1
		# get the square root of the accumulator
		elif instruction == "s":
			accumulator **= 2
		# print the accumulator
		elif instruction == "o":
			print(accumulator, end="")
		# compile the accumulator values to string.
		elif instruction == "c":
			print(chr(accumulator), end="")
		# reset the accumulator
		elif instruction == "r":
			accumulator = 0

		# set the accumulator to 0 if it's bigger than 256 or less than 0
		if accumulator == 256 or accumulator == -1:
			accumulator = 0
		
		pointer += 1


def get_file(filename):
	f = open(filename, "r")
	interpreter(f.read())
	f.close()

# the main function
def main():
	if len(sys.argv) == 2:
		get_file(sys.argv[1])
	else:
		source = input("Please type your brainf*ck code: ")
		interpreter(source)


# run the main function when the program has finished loading
if __name__ == "__main__": 
	main()