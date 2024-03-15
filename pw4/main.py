import math
import os
from input import input_studentNum, input_courseNum, input_studentInfo, input_courseInfo
from output import student_list, course_list, studentmark_courseInfo
from domains import Students, Courses

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def main(self):
        student_num = input_studentNum()
        for _ in range(student_num):
            name, student_id, dob = input_studentInfo()
            student = Students(name, student_id, dob)
            self.students.append(student)

        course_num = input_courseNum()
        for _ in range(course_num):
            name, course_id = input_courseInfo()
            course = Courses(name, course_id)
            self.courses.append(course)

        for student in self.stduents:
            for course in self.courses:
                student.inputMarks(course)

    course_credits = {course.id: float(input(f"Enter credtis for {course.name}: ")) for course in self.courses}

