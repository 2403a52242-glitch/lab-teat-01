class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Student Details:")
        print(f"Name    : {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Marks   : {self.marks}")

# Example usage:
if __name__ == "__main__":
    # You can change these values to test with different students
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = Student(name, roll_no, marks)
    student.display_details()
