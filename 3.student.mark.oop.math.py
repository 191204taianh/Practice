import math
import numpy as np

class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.id = student_id
        self.dob = dob
        self.marks = {}

    def inputMarks(self, course):
        marks = float(input(f"Enter mark for {course.name} for student {self.name}: "))
        marks = math.floor(marks * 10) / 10
        self.marks[course.id] = marks
    
    def calGPA(self, course_credits):
        total_credits = sum(course_credits.get(course_id, 0) for course_id in self.marks)
        if total_credits == 0:
            return 0
        weighted_sum = sum(self.marks.get(course_id, 0) * course_credits.get(course_id, 0) for course_id in self.marks)
        return weighted_sum / total_credits
    
class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.id = course_id

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
    
    def input_studentNum(self):
        return int(input("Enter the number of student: "))
    
    def input_courseNum(self):
        return int(input("Enter the number of courses: "))
    
    def input_studentInfo(self):
        return Student(input("Enter student's name: "),
                       input("Enter student ID: "),
                       input("Enter student DOB (DD-MM-YYYY: "))
    
    def input_courseInfo(self):
        return Course(input("Enter course's name: "),
                      input("Enter course ID: "))
    
    def student_list(self):
        print("Student list: ")
        for student in self.students:
            print(f"Student ID: {student.id: <10} | Student name: {student.name: <20} | Student DOB: {student.dob}")

    def course_list(self):
        print("Course list: ")
        for course in self.courses:
            print(f"Course ID {course,id: <10} | Course name: {course.name}")

    def studentMarks_courseInfo(self, student, course):
        print(f"Student : {student.name} -> Course: {course.name}")
        marks = student.marks.get(course.id, "Marks not available")
        print(f"Marks: {marks}")

    def main(self):
        student_num = self.input_studentNum()
        for _ in range(student_num):
            student_info = self.input_studentInfo()
            self.students.append(student_info)

        course_num = self.input_courseNum()
        for _ in range(course_num):
            course_info = self.input_courseInfo()
            self.courses.append(course_info)

        for student in self.students:
            for course in self.courses:
                student.inputMarks(course)

        course_credits = {course.id: float(input(f"Enter creadits for course {course.name}: ")) for course in self.courses}
        for student in self.students:
            gpa = student.calGPA(course_credits)
            print(f"Average GPA for student {student.name} is: {gpa: .2f}")

        self.students.sort(key = lambda student: student.calGPA(course_credits), reverse = True)
        print("Students sorted by GPA descending: ")
        for student in self.students:
            print(f"Student ID: {student.id: <10} | Student name {student.name: <20} | Student DOB: {student.dob}")

        choose_student = input("\nChoose one student to show mark (Student ID): ")
        choose_course = input("Choose a course to show mark: ")

        selected_student = next((student for student in self.students if student == choose_student), None)
        selected_course = next((course for course in self.courses if course == choose_course), None)

        if selected_student and selected_course:
            self.studentMarks_courseInfo(selected_student, selected_course)
        else:
            print("No student or mark available in the list!!!")

school_system = SchoolSystem()
school_system.main()