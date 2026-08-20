from .person import Person


class Doctor(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display_info(self):
        return f"{self.name} | {self.department}"