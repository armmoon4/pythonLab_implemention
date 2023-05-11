class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.courses = []
        self.semester = 1
        self.total_credit_hours = 0
        self.total_grade_points = 0
        self.cgpa = 0
        self.liability_statement = ""

    def add_course(self, course_name, credit_hours, grade_point):
        self.courses.append((course_name, credit_hours, grade_point))
        self.total_credit_hours += credit_hours
        self.total_grade_points += (credit_hours * grade_point)
        self.cgpa = self.total_grade_points / self.total_credit_hours

    def set_liability_statement(self, statement):
        self.liability_statement = statement

    def set_coursedetails(self):
        coursedetails = f"coursedetails for {self.name} (Roll Number: {self.roll_number})\n\n"
        coursedetails += f"Semester: {self.semester}\n\n"
        coursedetails += "Course Details:\n"
        for course in self.courses:
            coursedetails += f"{course[0]} ({course[1]} credit hours): {course[2]}\n"
        coursedetails += "\n"
        coursedetails += f"Total Credit Hours: {self.total_credit_hours}\n"
        coursedetails += f"Total Grade Points: {self.total_grade_points}\n"
        coursedetails += f"CGPA: {self.cgpa}\n\n"
        coursedetails += "Liability Statement:\n"
        coursedetails += self.liability_statement
        return coursedetails


student = Student("Md Abdur Rahman", "213-15-4343")
student.set_liability_statement("Father Name:Mazed Ali , Phone Number:01712061784")
student.add_course("OOP", 3, 3.0)
student.add_course("PPS", 2, 3.0)
student.add_course("OOP2", 3, 3.25)
print(student.set_coursedetails())
