import os
import csv
#import basic modules

#read our csv file
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	#get the header out of the way
	csvheader = next(csvreader)

	#define basic variables
	months=0
	total=0

	#we have no idea what our profits/losses are like, so we need to define a greatest increase/decrease that we know to be within our data set. So we manually do the first month
	first = next(csvreader)
	months=months+1
	total=total+int(first[1])
	biginc=int(first[1])
	bigdec=int(first[1])
	bigincmonth=first[0]
	bigdecmonth=first[0]


	#now we run for the rest of the months, cumulating a total and keeping track of any larger or smaller values. We also add any months with equally large/small profits/losses to our string in our elseif
	for row in csvreader:
		months+=1
		total=total+int(row[1])
		if biginc<int(row[1]):
			biginc=int(row[1])
			bigincmonth = row[0]
		elif biginc==int(row[1]):
			bigincmonth = bigincmonth + ", " + row[0] #handle case for ties
		if bigdec>int(row[1]):
			bigdec=int(row[1])
			bigdecmonth=row[0]
		elif bigdec==int(row[1]):
			bigdecmonth = bigdecmonth + ", " + row[0] #likewise for more ties


#now we print our values
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: "+'${:,.0f}'.format(total))
print(f"Average Change: "+'${:,.2f}'.format(total/months))
print(f"Greatest Increase in Profits: {bigincmonth} ({'${:,.0f}'.format(biginc)})")
print(f"Greatest Decrease in Profits: {bigdecmonth} ({'${:,.0f}'.format(bigdec)})")


#and write them to a text file
file = open("Financial Analysis.txt","w")
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {months}\n")
file.write(f"Total: "+'${:,.0f}'.format(total)+"\n")
file.write(f"Average Change: "+'${:,.2f}'.format(total/months)+"\n")
file.write(f"Greatest Increase in Profits: {bigincmonth} ({'${:,.0f}'.format(biginc)})\n")
file.write(f"Greatest Decrease in Profits: {bigdecmonth} ({'${:,.0f}'.format(bigdec)})\n")
file.close()