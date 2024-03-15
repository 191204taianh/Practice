def student_list(students):
    print("Student list: ")
    for student in students: 
        print(f"Student ID: {student.id: <10} | Student name: {student.name: <20} | Student DOB: {student.dob}")

def course_list(courses):
    print("Course list: ")
    for course in courses:
        print(f"Course ID: {course.id: <10} | Course name: {course.name}")

def studentmark_courseInfo(student, course):
    print(f"\nStudent: {student.name} -> Course: {course.name}")
    marks = student.marks.get(course.id, "Marks not available")
    print(f"Marks: {marks}")
