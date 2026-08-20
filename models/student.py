from .person import Person


class Student(Person):
    def __init__(self, name, id, major):
        super().__init__(name)
        self.id = id
        self.major = major
        self.courses = []

    def add_courses(self, course):
        self.courses.append(course)

    def display_info(self):
        courses_str = ", ".join(
            [f"{c.course_name} ({c.doctor.name})" for c in self.courses]
        )
        return f"{self.name} | {self.id} | {self.major} | Courses: {courses_str}"