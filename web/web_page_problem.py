inputFile = open('TWSP_small(1).txt', 'r')

#TWSP_large.txt
#TWSP_small(1).txt
#TWSP_large(1).txt
#small.txt

# The first input is the number of websites
website_count = inputFile.readline()

#Make a 2d array to store all the data
All_detail = []

for i in range(int(website_count)):
	# read one line
	detail=inputFile.readline()
	#take out the new line var '\n'
	detail=detail.strip()
	#make a list
	detail = detail.split()
	#convert to string
	detail = [int(x) for x in detail] 
	#add to 2d array
	All_detail.append(detail)


#close the file data was fached from
inputFile.close()
#sort the data using the first colume count

All_detail = sorted(All_detail,key=lambda x: (x[0], -x[1]))

# Right our output here
file1 = open('output.txt', 'w')
for detail in All_detail:
	detail_str = [str(x) for x in detail]
	detail_str = ','.join(detail_str)
	#print(d)
	file1.writelines(detail_str)
	file1.writelines('\n')
	
file1.close()

