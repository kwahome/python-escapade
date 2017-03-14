import sys
from collections import OrderedDict

brackets_dict = {
					'angled_bracket_open':'<',					
					'angled_bracket_closed':'>',
					'curly_bracket_open':'{',
					'curly_bracket_closed':'}',
					'round_bracket_open':'(',
					'round_bracket_closed':')',
					'square_bracket_open':'[',
					'square_bracket_closed':']'					
				}

brackets_count = {
					'angled_bracket_open':0,					
					'angled_bracket_closed':0,
					'curly_bracket_open':0,
					'curly_bracket_closed':0,
					'round_bracket_open':0,
					'round_bracket_closed':0,
					'square_bracket_open':0,
					'square_bracket_closed':0					
				}

def check_parenthesis(brackets_dict, brackets_count, input_text):

	brackets_dict = OrderedDict(sorted(brackets_dict.items(), key=lambda t: t[0]))
	brackets_count = OrderedDict(sorted(brackets_count.items(), key=lambda t: t[0]))

	for char in input_text:
		for key, value in brackets_dict.iteritems():
			if char == value:
				brackets_count[key] += 1
			else:
				brackets_count[key] = brackets_count[key]

	return brackets_count

def show(report):
	for key, value in report.iteritems():
		print " |-> " + value + " " + key


	
def main(fname):
	

	# concatenate the folder location and the file name and extension to form a path 
	input_path = "input/"+fname

	# try statement
	try:		

		# Open the input file in read mode
		read_file = open(input_path, 'r')

		print "BALANCED BRACKET CHECK REPORT:"
		print "\n"

		# Read the file content line by line
		for line_number, line in enumerate(read_file):
			
			if line.strip() == '':
				print "[LINE " + str(line_number) + "] : New line"
			else:
				results = check_parenthesis(brackets_dict, brackets_count,line)
				
				input_okay = True
				report = {}

				i = 0
				j = i+1

				while i <= len(results)/2+1:
					bracket = results.items()[i][0].split('_')
					bracket_name = bracket[0]+" "+bracket[1]+"s"

					if results.items()[i][1] == results.items()[j][1]:
						response = "Found " + str(results.items()[j][1]) + " open " + ", " + str(results.items()[i][1]) + " closed "
					else:
						input_okay = False
						response = "Found " + str(results.items()[j][1]) + " open " + ", " + str(results.items()[i][1]) + " closed "

					# Update the results in the data_dict
					report.update({bracket_name : response})
					i = j+1
					j = i+1

				if input_okay:
					message = "Balanced brackets"
				else:
					message = "Unbalanced brackets found"
				
				print "[LINE " + str(line_number) + "] : " + message
				show(report)

	# Handle exceptions
	except:
		print "Could not proceed because of:"
		print "~ The file "+fname+" does not exist"
		print "Please supply the correct file name and run again"

if __name__ == "__main__":

	try:
		sys.exit(main(sys.argv[1]))

	except Exception:
		print "An error has occured"
		print "To run this program, the name of the file to be read should be passed as a parameter"
		print "For instance, python balanced_parenthesis.py file.py"
