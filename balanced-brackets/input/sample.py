import sys

def main(n):
	n= int(n)

	fibonacci_series = [0,1]

	for i in range(1,n-1):
		next_fibonacci_no = fibonacci_series[(len(fibonacci_series)-1)]+fibonacci_series[(len(fibonacci_series)-2)]
		fibonacci_series.append(next_fibonacci_no)

	print fibonacci_series

if __name__ == "__main__":
	try:
		sys.exit(main(sys.argv[1]))

	except Exception:
		print "An error has occured"
		print "To run this program, the number of Fibonacci numbers to be generated should be passed as a parameter"
		print "For instance, python weather fibonacci.py 5"