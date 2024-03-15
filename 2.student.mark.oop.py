class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.id = student_id
        self.dob = dob
        self.marks = {}

    def input_mark(self, course):
        marks = float(input(f"Enter mark for {course.name} for student {self.name}: "))
        self.marks[course.id] = marks

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
        return int(input("Enter the number of course: "))
    
    def input_studentInfo(self):
        return Student(input("Enter student name: "),
                       input("Enter the student ID: "),
                       input("Enter the student DOB: "))
    
    def input_courseInfo(self):
        return Course(input("Enter the course name: "),
                      input("Enter the course ID: "))
    
    def student_list(self):
        print("\n--------------------")
        print("Student list: ")
        print("--------------------")
        for student in self.students:
            print(f"Student ID: {student.id: <10} | Student name: {student.name: <20} | Student DOB: {student.dob}")

    def course_list(self):
        print("\n--------------------")
        print("Course list: ")
        print("--------------------")
        for course in self.courses:
            print(f"Course ID: {course.id: <10} | Course name: {course.name}")

    def studentMark_courseInfo(self, student, course):
        print(f"\nStudent: {student.name} -> Course: {course.name}")
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
                student.input_mark(course)

        self.student_list()
        self.course_list()

        choose_student = input("Enter the student to get mark (Student ID): ")
        choose_course = input("Enter the course to show mark (Course ID): ") 

        selected_student = next((student for student in self.students if student.id == choose_student), None)
        selected_course = next((course for course in self.courses if course.id == choose_course), None)

        if selected_student and selected_course:
            self.studentMark_courseInfo(selected_student, selected_course)
        else:
            print("No stuent or course available!!!")

school_system = SchoolSystem()
school_system.main()