import os
import csv
#importing basic modules

#read our csv file
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	#get the header out of the way
	csvheader = next(csvreader)

	#define basic variables
	votes=0
	candidates={}

	#count the votes
	for row in csvreader:
		votes+=1
		#here if we have a new candidate we add a new entry in our dictionary
		if row[2] not in  candidates:
			candidates[row[2]] = 1
		#here if the candidate is already voted for we add 1 to their vote count
		elif row[2] in candidates:
			candidates[row[2]]+=1

#we define some variables to figure out who won
high=0
winner=""
#in the event of a tie we can add names to our winner statement below
tie=""
#find the winner
for c,v in candidates.items():
	if v>high:
		high=v
		winner=c
		tie="" #don't forget to correct for any earlier joint leaders
	elif v==high:
		winner=winner+", "+c
		tie="s"


#now we print out our results
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {votes}")
print("-------------------------------")
for c,v in candidates.items():
	print(f"{c}: ({'{:.3%}'.format(v/votes)} {v})")
print("-------------------------------")
print(f"Winner{tie}: {winner}")
print("-------------------------------")

#and write them to a text file
file = open("Election Results.txt","w")
file.write("Election Results\n")
file.write("-------------------------------\n")
file.write(f"Total Votes: {votes}\n")
file.write("-------------------------------\n")
for c,v in candidates.items():
	file.write(f"{c}: ({'{:.3%}'.format(v/votes)} {v})\n")
file.write("-------------------------------\n")
file.write(f"Winner{tie}: {winner}\n")
file.write("-------------------------------\n")