"""Student Management System: stores and manages student records."""


class Student:
    """A single student record."""

    def __init__(self, roll_no, name, email, course):
        self.roll_no = roll_no
        self.name = name
        self.email = email
        self.course = course

    def __repr__(self):
        return f"Student({self.roll_no}, {self.name!r}, {self.email!r}, {self.course!r})"


class StudentManager:
    """Keeps student records in memory, indexed by roll number."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.roll_no in self.students:
            raise ValueError(f"Student with roll no {student.roll_no} already exists")
        self.students[student.roll_no] = student
        return student

    def get_student(self, roll_no):
        return self.students.get(roll_no)

    def remove_student(self, roll_no):
        if roll_no not in self.students:
            raise KeyError(f"No student with roll no {roll_no}")
        return self.students.pop(roll_no)

    def list_students(self):
        return sorted(self.students.values(), key=lambda s: s.roll_no)

    def count(self):
        return len(self.students)


if __name__ == "__main__":
    manager = StudentManager()
    manager.add_student(Student(1, "Aarav Sharma", "aarav.sharma@vcet.edu.in", "AI&DS"))
    manager.add_student(Student(2, "Priya Patil", "priya.patil@vcet.edu.in", "AI&DS"))
    manager.add_student(Student(3, "Rohan Mehta", "rohan.mehta@vcet.edu.in", "COMP"))
    for s in manager.list_students():
        print(s)
    print("Total students:", manager.count())
