import random
from copy import deepcopy
import Comparison, Student, Lecture
import pprint
import json
import ast

def lectureFit(lectureTime, studentAvailability):
    #for i in lectureTime:
    #    for j in lectureTime[i]:

    return


def decideOrder():
    """ Helper function """
    decision = random.randint(1, 2)
    return decision
  
 


def calculateTime(studentList, lectureList):
    stu = deepcopy(studentList)
    lec = deepcopy(lectureList)
    totalClasses = 0
    random.shuffle(stu)
    random.shuffle(lec)
    for index in range(len(stu)):
        numClasses = 0
        for j in range(len(lec)):
            
            sTime = stu[index].get_avail_table().get_matrix()
            #print("Running" + str(index))
                
            if decideOrder() == 1 and lec[j].get_number1() < 20:
                lTime = lec[j].get_schedule1().get_matrix()
                if Comparison.compare(sTime, lTime):  # check if time fit
                    Comparison.minus(sTime, lTime)
                    stu[index].add_class([lec[j].get_id(), lec[j].get_time1(),lec[j].get_name()])
                    numClasses += 1
                    totalClasses += 1
                    lec[j].add_student1()
                    if numClasses >= 5:
                        break
                elif lec[j].get_number2() < 20:
                    lTime = lec[j].get_schedule2().get_matrix()
                    if Comparison.compare(sTime, lTime):  # check if time fit
                        Comparison.minus(sTime, lTime)
                        stu[index].add_class([lec[j].get_id(), lec[j].get_time2(), lec[j].get_name()])
                        numClasses += 1
                        totalClasses += 1
                        lec[j].add_student2() 
                        if numClasses >= 5:
                            break
                        
            elif lec[j].get_number2() < 20:
                lTime = lec[j].get_schedule2().get_matrix()
                if Comparison.compare(sTime, lTime):
                    Comparison.minus(sTime, lTime)

                    stu[index].add_class([lec[j].get_id(), lec[j].get_time2(), lec[j].get_name()])
                    numClasses += 1
                    totalClasses += 1
                    lec[j].add_student2() 
                    if numClasses >= 5:
                        break
                elif lec[j].get_number1() < 20:
                    lTime = lec[j].get_schedule1().get_matrix()
                    if Comparison.compare(sTime, lTime):
                        Comparison.minus(sTime, lTime)
                        stu[index].add_class([lec[j].get_id(), lec[j].get_time1(), lec[j].get_name()])
                        numClasses += 1
                        totalClasses += 1
                        lec[j].add_student1() 
                        if numClasses >= 5:
                            break
                
            elif lec[j].get_number1() < 20:
                lTime = lec[j].get_schedule1().get_matrix()
                if Comparison.compare(sTime, lTime):
                    Comparison.minus(sTime, lTime)
                    stu[index].add_class([lec[j].get_id(), lec[j].get_time1(), lec[j].get_name()])
                    numClasses += 1
                    totalClasses += 1
                    lec[j].add_student1() 
                    if numClasses >= 5:
                        break
   

    return [totalClasses, stu, lec]


def runThrough(studentList, lectureList):
    MAX = 100
    PC = 0
    currentBest = 0
    while currentBest < 390:
        res = calculateTime(studentList, lectureList)
        if res[0] > currentBest:
            currentBest = res[0]
            finalRes = res
        PC += 1
    print (finalRes[0])
    print (4312513582965871324795642965107831)
    return finalRes


def printSchedule(studentList):
    for index in range(len(studentList)):
        id = studentList[index].get_id()
        lectureid = studentList[index].get_class()
        print (id)
        print (lectureid)
        print ()
        index += 1

def jsonSchedule(studentList):
    
    studentList.sort(key=lambda x: int(x.get_id()))
    jsonDict = {}
    for index in range(len(studentList)):
        id = studentList[index].get_id()
        lectureid = studentList[index].get_class()
        studentDict={}
        for i in range(len(lectureid)):
            tempDict = {}
            tempDict = ast.literal_eval(str(lectureid[i][1]))
            newTempDict = {}
            newTempDict.update({"name":lectureid[i][2]})
            newTempDict.update({"time":tempDict})
            studentDict.update({lectureid[i][0]:newTempDict})
        
        jsonDict.update({id: [studentList[index].get_name(), studentDict]})
    print(jsonDict)
    
    with open('data.json', 'w') as outfile:
        json.dump(jsonDict, outfile, indent=4)
    