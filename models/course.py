class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.doctor = None
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def set_doctor(self, doctor):
        self.doctor = doctor