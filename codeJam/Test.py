import MatrixComparison, Student, Lecture

print("starting")

m = MatrixComparison


something = m.runThrough(Student.get_students(), Lecture.get_lectures())

#m.printSchedule(something[1])



m.jsonSchedule(something[1])

print (something[0])