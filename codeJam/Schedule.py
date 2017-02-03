class Schedule(object):
    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    def __init__(self,matrix):
        self.matrix = matrix
        
    def get_matrix(self):
        return self.matrix
    
    def print_m(self):
        print(self.get_matrix())
    
def make_schedule(time, matrix):
    #print(time)
    table = to_schedule(time, matrix)
    schedule = Schedule(table)
    return schedule
    #matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def make_schedule_lecture(time):
    #print(time)
    table = to_schedule_lecture(time)
    schedule = Schedule(table)
    return schedule

def to_schedule(time,matrix):
   # matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    day = time["day"]
    if day == "Monday":
        index = 0
    elif day == "Tuesday":
        index = 1
    elif day == "Wednesday":
        index = 2
    elif day == "Thursday":
        index = 3
    elif day == "Friday":
        index = 4
        
    for x in range(5):
        if x == index:
            start = convert_time(time["start"])
            end = convert_time(time["end"])
            while start<end :
                matrix[x][start] = 1
                start += 1
    return matrix

def to_schedule_lecture(time):
    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    day = time["day"]
    if day == "Monday":
        index = 0
    elif day == "Tuesday":
        index = 1
    elif day == "Wednesday":
        index = 2
    elif day == "Thursday":
        index = 3
    elif day == "Friday":
        index = 4
        
    for x in range(5):
        if x == index:
            start = convert_time(time["start"])
            end = convert_time(time["end"])
            while start<end :
                matrix[x][start] = 1
                start += 1
    return matrix

            
def convert_time(time):
    if len(time)<7 and len(time)>2 :
        timeIn24 = time[0:1] + time[2:4]
    elif len(time)<=2:
        timeIn24 = "0800"
    else:
        timeIn24 = time[0:2] + time[3:5]
    timeInt = int(timeIn24)
    
    if time[0] != "N":
        if time[5] == "p":
            timeInt = timeInt + 1200
    if timeInt>=2400:
        timeInt -= 1200
        
    if timeInt<800:
        timeInt = 800
    elif timeInt > 1700:
        timeInt = 1700
    timeInt -= 800
    i = int(2*timeInt/100)
    if timeInt%100 != 0:
        i += 1
    #print(i)
    return i

#print(to_schedule({'start': '08:30am', 'end': '03:30pm', 'day': 'Monday'}))
#convert_time("01:30pm")
