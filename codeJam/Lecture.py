import jsonReader
import Schedule
from test.test_print import ClassWith__str__
matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
class Lecture(object):
    idNumber = ""
    name = ""
    time_one = ""
    time_two = ""
    session_one = Schedule.Schedule(matrix)
    session_two = Schedule.Schedule(matrix)
    number_students_one = 0
    number_students_two = 0
  
    def __init__(self, idNumber, name, time_one, time_two, session_one, session_two):
        self.idNumber = idNumber
        self.name = name
        self.time_one = time_one
        self.time_two = time_two
        self.session_one = session_one
        self.session_two = session_two
        
    def get_time1(self):
        return  self.time_one
    
    def get_time2(self):
        return self.time_two
    
    def get_id(self):
        return self.idNumber
    
    def get_name(self):
        return self.name
    
    def get_schedule1(self):
        return self.session_one
    
    def get_schedule2(self):
        return self.session_two
    
    def get_number1(self):
        return self.number_students_one
    
    def get_number2(self):
        return self.number_students_two
       
    def add_student1(self):
        self.number_students_one += 1
    
    def add_student2(self):
        self.number_students_two += 1
    
    def print_l(self):
        print("id:" , self.idNumber , "  name:" , self.name , "  time1:" , self.time_one , "  time2:" , self.time_two) 
        
def make_lecture(idNumber, name, time_one, time_two, session_one, session_two):
    lecture = Lecture(idNumber, name, time_one, time_two, session_one, session_two)
    return lecture


    
def get_lectures():
    classes = []
    data = jsonReader.getLecture()
    for x in range(10):
        time1 = data["classes"][str(100+x+1)]["times"]["time1"]
        time2 = data["classes"][str(100+x+1)]["times"]["time2"]
        classes.append(make_lecture(str(100+x+1), data["classes"][str(100+x+1)]["name"],time1, time2,Schedule.make_schedule_lecture(time1), Schedule.make_schedule_lecture(time2)))
        #classes[x].print_l()
        #classes[x].get_schedule1().print_m()
        #classes[x].get_schedule2().print_m()
    return classes
 
#get_lectures()

