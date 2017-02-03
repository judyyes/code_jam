def comparator(smallStudentTime, smallLectureTime):
    if smallStudentTime[0] == smallLectureTime[0] and smallStudentTime[1] <= smallLectureTime[1] \
            and smallStudentTime[2] >= smallLectureTime[2]:
        return True
    return False
"""
def filler(studentAvailability, smallLectureTime):
    res = []
    for i in studentAvailability:
        if comparator(studentAvailability[i], smallLectureTime):
"""