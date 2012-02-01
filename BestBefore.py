# A challenge from Spotify to determine the most recent date.  I guess those ads really work!
# Anyways, this is 1)my first attempt and 2)my heavily delayed foray into Python.
# The full specs are at http://www.spotify.com/us/jobs/tech/best-before/  

# TODO: Use assert__stmt's to debug, catch some errors
# TODO: Should I brew install python3 and keep multipe versions around using virtual env's? 

import sys

# Initialize me some variables.  Is this necessary?
day = month = year = None

# Get the date
# input = raw_input("Enter a date: ")
input = sys.stdin.readline()

dates = input.split("/")
dates = [int(x) for x in dates]

# print[date for date in dates]
# print[type(date) for date in dates]


# Best case, year > 31
for date in dates:
	if date > 31:
		# Save the index of the year so we can remove it later
		idx = dates.index(date)

		# Does the year have 2 or 4 digits?
		if len(str(date)) == 2:
			date += 2000

		year = date 

		# Remove the year from list
		dates.pop(idx)



# Look for a match in the order: year, month, day

# Sort the list from smallest to biggest
dates.sort()

while dates:
	current = dates.pop(0) # Get the smallest value
	#print "popped", current
	
	if year == None:
		year = 2000 + current

	elif month == None and current < 13:
		month = current

	else:
		day = current


# Check if it's a legal date. ex: September only has thirty days.
legal = True

if day == 31:
	if month not in [1, 3, 5, 7, 8, 10, 12]:
		legal = False
		
elif day == 30:
	if month in [2]:
		legal = False

elif day == 29:
	# Check for a leap year
	if month in [2]:
		if year % 4 ==0:
			if year % 100 == 0 and year % 400 != 0:
				legal = False
		else:
			legal = False


# Print the result
if legal:
	sys.stdout.write("%d" % year)
	sys.stdout.write("-%02d" % month)
	sys.stdout.write("-%02d\n" % day)
else:
	sys.stdout.write("%s" % input.strip())
	sys.stdout.write(" is illegal\n")

