from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"



















#
# import sqlite3
#
#
# conn = sqlite3.connect('university.db')
# c = conn.cursor()
#
#
# c.execute('''
#     CREATE TABLE Department (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT
#     )
# ''')
#
#
# c.execute('''
#     CREATE TABLE Student (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         department_id INTEGER,
#         FOREIGN KEY (department_id) REFERENCES Department (id)
#     )
# ''')
#
# c.execute('''
#     CREATE TABLE Course (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         department_id INTEGER,
#         FOREIGN KEY (department_id) REFERENCES Department (id)
#     )
# ''')
#
#
# c.execute('''
#     CREATE TABLE Enrollment (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_id INTEGER,
#         course_id INTEGER,
#         enrollment_date DATE,
#         FOREIGN KEY (student_id) REFERENCES Student (id),
#         FOREIGN KEY (course_id) REFERENCES Course (id)
#     )
# ''')
#
#
# conn.close()


