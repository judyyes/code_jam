class TimeSpan(object):

    def __init__(self, day, starting, ending):
        self.day = day
        self.starting = starting
        self.ending = ending

    def timeToIndex(self, time):
        "Transform time in 00:00am format to a matrix index,\
        assuming the time is given in block of 30m"
        if time == "NA":
            return 0
        elif time[5] == "a":
            adjustment = 0
        elif time[5] == "p":
            adjustment = 12
        return int((int(time[0])*10+int(time[1])+adjustment)*2+int(time[3])/3)

    def dayToIndex(self, day):
        "Transform day of the week to a matrix index"
        if day == "Monday":
            res = 0
        elif day == "Tuesday":
            res = 1
        elif day == "Wednesday":
            res = 2
        elif day == "Thursday":
            res = 3
        elif day == "Friday":
            res = 4
        return res

    def matrixConstructor(self, matrixList, day, startingTime, endingTime):
        res = [3]
        res[0] = self.dayToIndex(day)
        if startingTime < self.timeToIndex("08:00am"):  # earliest class time at 8am
            startingTime = self.timeToIndex("08:00am")
        if endingTime > self.timeToIndex("05:00pm"):  # latest class time at 5pm
            endingTime = self.timeToIndex("05:00pm")
        if endingTime == 0:
            res[1] = 0
            res[2] = 0
            return res
        res[1] = startingTime
        res[2] = endingTime
        matrixList.append(res)
        return

        
ts = TimeSpan("Monday","08:00am", "09:00pm")    
print (ts.timeToIndex("08:00am"))
print (ts.dayToIndex("Tuesday"))