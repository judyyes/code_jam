import jsonReader
import Schedule
from builtins import int

matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
class Student(object):
    idNumber = ""
    name = ""
    available_day = []
    avail_time = Schedule.Schedule(matrix)
    #time = ""
    classesTaken = []
    
    def __init__(self, idNumber, name, available_day, avail_time):
        self.idNumber = idNumber
        self.name = name
        self.available_day = available_day
        self.avail_time = avail_time
        self.classesTaken = []
        
    def get_available_day(self):
        return  self.available_day
    
    def get_id(self):
        return self.idNumber
    
    def get_name(self):
        return self.name
       
    def get_avail_table(self):
        return self.avail_time
    
    def print_s(self):
        print("id:" , self.idNumber , "  name:" , self.name)
        length = len(self.available_day)
        for x in range(length):
            print("avail",str(x+1),self.available_day[x])
            
    def add_class(self, classID):
        self.classesTaken.append(classID)
    
    def get_class(self):
        return self.classesTaken
        
def make_Student(idNumber, name, available_day, avail_time):
    student = Student(idNumber, name, available_day, avail_time)
    return student

def get_avail_day(info):
    avail_day = []
    length = len(info)
    for x in range(length):
        #print(info["avail"+str(x+1)])
        avail_day.append(info["avail" + str(x+1)])
    return avail_day
        
'''Array of All the Students Objects'''
def get_students():
    students = []
    data = jsonReader.getName()
    for x in range(80):
        students.append(make_Student(str(x+1), data[str(x+1)][0], get_avail_day(data[str(x+1)][1]), build_avail_table(get_avail_day(data[str(x+1)][1]))))
        #students[x].print_s()
        #print(students[x].get_avail_table().print_m())
    return students

'''helper method'''
def build_avail_table(avail_day):
    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    avail_table = Schedule.Schedule(matrix)
    for x in range(len(avail_day)):
        avail_table = Schedule.make_schedule(avail_day[x],avail_table.get_matrix())
    return avail_table

#get_students()