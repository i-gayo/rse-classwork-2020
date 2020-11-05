import datetime

#Function that returns the start, end times for every interval specified 
def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):

    #Returns a datetime object corresponding to what sspecified in start_time string 
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") #Y-m specifies format of string specified
    print("Start time : ", start_time_s)
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    #Obtains the difference in times in seconds for every interval ; unsure what second half of the code does:  gap_between_intervals_s * (1 / number_of_intervals - 1)
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    
    #Tests to see if start time < end time to prevent negative time ranges 
    if start_time_s < end_time_s: 
        #Obtains the start_end time for every interval between the TOTAL_START and TOTAL_END times given as input; gap is the time between each interval in seconds
        # If no of intervals = 2: two second ranges are specified 
        sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                    start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                    for i in range(number_of_intervals)]
        print(sec_range)
        return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]
    else:
        raise ValueError("Start time should be before end time")

#Computes the overlapping times between the specified time ranges 
def compute_overlap_time(range1, range2):
    overlap_time = []

    #Obtain every start and times in timerange1 
    for start1, end1 in range1:
        #Obtains every start and times in timerange 2

        for start2, end2 in range2:
            #Obtains lowest, highest time between the two ranges 
            low = max(start1, start2)
            high = min(end1, end2)
            
            #Append in list of overlap times 
            overlap_time.append((low, high))
            
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00" , 2, 30)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 4, 60)
    print("Result is: " , len(compute_overlap_time(large, short)))

print("Hello")