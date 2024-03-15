students = []
courses = []

def input_studentNum():
    return int(input("Enter the number of students: "))

def input_courseNum():
    return int(input("Enter the number of courses: "))

def input_studentInfo():
    return {'name': input("Enter students' name: "),
            'student ID': input("Enter the student ID: "),
            'DOB': input("Enter the students' date of birth (DD-MM-YYYY): "),
            'marks': {}}

def input_courseInfo():
    return {'name': input("Enter the courses' name: "),
            'course ID': input("Enter the course ID: ")}

def input_studentMark(course):
    marks = float(input(f"Enter stuent mark for {course['name']} - {student['name']}: "))
    return marks

def student_list():
    print("\n------------------------------")
    print("Student list: ")
    print("------------------------------")
    for student in students:
        print(f"Student ID: {student['student ID'] : <10} | Student name: {student['name']: <30} | Student DOB: {student['DOB']}")

def course_list():
    print("\n------------------------------")
    print("Course list: ")
    print("------------------------------")
    for course in courses:
        print(f"Course ID: {course['course ID']} | Course name: {course['name']}")

def studentMark_courseInfo(student, course):
    print(f"\nStudent: {student['name']} -> Course: {course['name']}")
    marks = student['marks'].get(course['course ID'], "Marks not available")
    print(f"Mark: {marks}")

student = input_studentNum()

for _ in range(student):
    student_info = input_studentInfo()
    students.append(student_info)

course = input_courseNum()

for _ in range(course):
    course_info = input_courseInfo()
    courses.append(course_info)

for student in students:
    for course in courses:
        student['marks'][course['course ID']] = input_studentMark(course)

student_list()
course_list()

choose_student = input("\nChoose stuent to show mark (Student ID): ")
choose_course = input("Choose course to show mark (Course ID): ")

selected_student = next((student for student in students if student['student ID'] == choose_student), None)
selected_course = next((course for course in courses if course['course ID'] == choose_course), None)

if selected_student and selected_course:
    studentMark_courseInfo(selected_student, selected_course)

else: 
    print("No student or course available")