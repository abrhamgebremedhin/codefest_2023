from datetime import datetime, timedelta, time



#TT_large.txt
#TT_small(1).txt
#TWSP_large(1).txt
#small.txt

# new list to track many detail
worker_info=[]

# single worker information
# #clock_tracker,total_work_hour,break_tracker

def format_timedelta(td):
    # Calculate the total number of seconds in the duration
    total_seconds = td.total_seconds()
    
    # Calculate the number of days, hours, minutes, and seconds
    days, seconds = divmod(total_seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    
    # Format the duration as a string
    duration_str = f'{int(days)}:{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
    
    return duration_str

def time_operation(time1,time2,oper):

	# Convert time strings to datetime.time objects
	#print(str(time1)+oper+str(time2))
	time1 = datetime.strptime(time1, '%H:%M:%S').time()
	time2 = datetime.strptime(time2, '%H:%M:%S').time()

	# Calculate the time difference

	if oper == '-':
		delta = timedelta(hours=time1.hour, minutes=time1.minute, seconds=time1.second) - timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
	if oper == '+':
		delta = timedelta(hours=time1.hour, minutes=time1.minute, seconds=time1.second) + timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
	# Format the result as a time string
	print('-<')
	print(delta)
	result = str(delta).split('.')[0]  # remove microseconds
	print('->')
	result_time = format_timedelta(delta)
	result_time = time(*map(int, result_time.split(':')))
	xx = str(result_time)
	print(xx[3:])
	# Print the result
	print(result_time)
	return result_time.strftime('%H:%M:%S')

def single_worker_detail(worker_detail):
	clock_tracker=''
	total_work_hour='00:00:00'
	break_tracker=''
	date=''
	start_time=''
	end_time=''
	# 0 	 1 			2 		  3
	# Emp_1  2019-06-04 10:28:25  clock-in
	for detail in worker_detail:
		#clock_tracker,total_work_hour,break_tracker,date
		#vars, -> total time,start_time,end_time

		## first open with clock-in start_time = clock-in
		if detail[3] == 'clock-in':
			if clock_tracker == 'clock-in':
				temp_data = time_operation('13:00:00',detail[2],'-')
				if temp_data > '06:00:00':
					total_work_hour = time_operation(total_work_hour,'06:00:00','+')
				else:
					total_work_hour = time_operation(total_work_hour,temp_data,'+')

				start_time = detail[2]
				date = detail[1]
				clock_tracker=detail[3]
				continue
			else:
				start_time = detail[2]
				end_time = ''
				date = detail[1]
				clock_tracker=detail[3]
				continue

		## if clock-in and date not same then 
			#do 13:00-start_time 
			#if number is greater than 6 then add 6 to total
			#if number is less than 6 then add the number
			#set clock-in time as start_time (start_time = clock-in)
		
		## if break-start then end_time = break-start
		## add to total
		## end_time = 0
		if detail[3] == 'break-start':
			end_time = detail[2]
			sub = time_operation(end_time,start_time,'-')
			total_work_hour = time_operation(total_work_hour,sub,'+')
			break_tracker=detail[3]
			continue

		
		## if break-stop then start_time = break-stop
		if detail[3] == 'break-stop':
			start_time = detail[2]
			end_time = ''
			break_tracker=detail[3]
			continue

		## if clock-out => end_time = clock-out
		if detail[3] == 'clock-out':
			end_time = detail[2]
			sub = time_operation(end_time,start_time,'-')
			total_work_hour = time_operation(total_work_hour,sub,'+')
			clock_tracker=detail[3]
			continue


	return total_work_hour


def main():
	inputFile = open('small.txt', 'r')
	# The first input is the number of websites
	log_count = inputFile.readline()

	#Make a 2d array to store all the data
	All_detail = []

	for i in range(int(log_count)):
		# read one line
		detail=inputFile.readline()
		#take out the new line var '\n'
		#print(detail)
		detail=detail.strip()
		#make a list
		
		detail = detail.split()
		#convert to string
		#print(detail)
		All_detail.append(detail)

	inputFile.close()
	#sort the data using the first colume count (worker name)

	All_detail = sorted(All_detail,key=lambda x: (x[0]))

	#To know the number of workers
	new_detail = [x[0] for x in All_detail]
	worker_name = set(new_detail)
	worker_name = sorted(worker_name)

	newx = []

	for i in worker_name:
		newx = one_worker_detail = [x for x in All_detail if x[0] == i]
		for i in newx:
			print(i)
		print('***************************************************************')

	for i in worker_name:
		one_worker_detail = [x for x in All_detail if x[0] == i]
		#print("-----+=+=->")
		temp = single_worker_detail(one_worker_detail)
		worker_info.append(temp)
		print('---------------------------------------------')
		print(temp)
		print('done')
		print('---------------------------------------------')


if __name__ == "__main__":
    main()



	



# # new list to track many detail
# worker_info=[]

# # single worker information
# # #clock_tracker,total_work_hour,break_tracker

# info = [0,0,0]

# for i in len(worker_number):
# 	worker_info.append(info)

# for detail in All_detail:
# 	print(detail)


#clock_tracker,total_work_hour,break_tracker
#print(new_detail)

