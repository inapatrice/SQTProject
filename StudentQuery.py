# Ina Patrice Gonzales
# December 7, 2020 
# Programming with Python
# Final Project (students.txt)
# Description: Program reads in a data file and manipulates that data depending upon user input then prints to screen.
# Uses lists, for loops, and built in functions 
 
# DATA FILE INPUT
# function that reads in a file and returns a list of lists of data 
# list does not include the header record
def readRecords(filename):
	result = []
	f = open(filename,'r')
	for line in f:
		line = line.rstrip('\n')
		fields = line.split('\t')
		result.append(fields)
	f.close()
	del result[0] # deletes the first element in the result list (header record)
	return result

# string that is used for output purposes
separator = '====================================================================================================================='

# FUNCTION DECLARATIONS 
# fucntion that prints out the given queries
def showOptions():
	print (separator)
	print ("Welcome to the Student Query Tool (SQT) Program!")
	print (separator)
	print ("Here are the possible queries.")
	print ("1. Display all student records.")
	print ("2. Display students whose last name begins with a certain string (case insensitive).")
	print ("3. Display all records for students whose graduating year is a certain year.")
	print(separator)
	print ("Please enter a number that coincides with your desired query or 'quit' to exit the program.")
	print(separator)

# function that will print a table for a given list in rows and columns
def printRecords(list):
	# headerList to be added to the given list
	header = ['ID', 'Last', 'First', 'GradYear','GradTerm','DegreeProgram']
	list.insert(0,header)
	# gets the length of the list and columns to print out equally
	lengthList = [len(sublist)for row in list for sublist in row]
	column = max(lengthList)
	for rows in list:
		rows = "".join(sublist.ljust(column+2) for sublist in rows)
		print (rows)
	del list[0] #removes the header
	return (separator)

# QUERY 1
# function that will display all student records
def allRecords(list):
	return(printRecords(list))

# QUERY 2
# function that will display last names with a certain string 
def lastNames(list):
	lastNameList = []
	search = str(input("Enter Last Name: "))
	# for loop that looks through list
	for sublist in list:
		#converts list and search string to lowercase 
		search = search.lower()
		sublist[1] = sublist[1].lower()
		#if the search string is in last name list
		if search.lower() in sublist[1].lower():
			# if last name starts with the search string, capitalize, and append to lastNameList
			if sublist[1].startswith(search):
				sublist[1] = sublist[1].capitalize()
				lastNameList.append(sublist)
		sublist[1] = sublist[1].capitalize()
	# if last name does not exist
	if not lastNameList: 
		return ('No last name found. Try again.')
	else: 
		return(printRecords(lastNameList))

# QUERY 3
# function that will display graduating in a certain year 
def gradYear(list):
	gradYearList = []
	search = str(input("Enter School Year: "))
	# for loop that looks through list
	for sublist in list:
		# if search string exists in year list
		if search in sublist[3]:
			gradYearList.append(sublist)
	# if school year is not in list
	if not gradYearList:
		return ("No school year found. Try again.")
	else:
		return(printRecords(gradYearList))

# function that takes in a user's input then outputs the corresponding query
def SQT():
	# studentRecords is now a list of lists from the given txt file -- students.txt
	studentRecords = readRecords("students.txt")
	breakList = ['quit','q']
	#infinite loop that will only break if user enters a string from the breakList  
	while True:
		showOptions()
		userInput = input("User Input: ")
		# if user enters a string from breakList
		if (userInput.lower() in breakList or userInput.upper() in breakList):
			break
		# if user enters a number that is not an option
		elif (userInput != '1' and userInput != '2' and userInput != '3'):
			print ("You have selected an incorrect option. Please try again.")
			print (separator)
		# if user enters a valid option
		else:  
			print ('You have selected option:', userInput)
			print(separator)
			if (userInput == '1'):
				print ("1. Display all student records.")
				print(separator)
				print (allRecords(studentRecords))
			elif (userInput == '2'):
				print ("2. Display students whose last name begins with a certain string (case insensitive).")
				print(separator)
				print (lastNames(studentRecords))
			elif (userInput == '3'):
				print ("3. Display all records for students whose graduating year is a certain year.")
				print(separator)
				print (gradYear(studentRecords))

# main function of the program
if __name__ == "__main__":
	SQT()
