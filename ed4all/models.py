from django.db import models
from decimal import Decimal

class Student_Advisor_Counselor(models.Model):
    Counselor_ID = models.CharField(primary_key=True, max_length=8, default="")
    Counselor_Name = models.CharField(max_length=45)
    C_Email = models.CharField(max_length=45, default="")
    def __str__(self):
        return self.Counselor_Name


class Student(models.Model):
    Student_ID = models.CharField(primary_key=True, max_length=8, default="")
    Student_Name = models.CharField(max_length=45)
    S_Email = models.CharField(max_length=45, default="")
    Counselor_ID = models.ForeignKey(Student_Advisor_Counselor)
    def __str__(self):
        return self.Student_Name

class Faculty (models.Model):
    Faculty_ID = models.CharField(primary_key=True, max_length=8, default="")
    Faculty_Name = models.CharField(max_length=45)
    F_Email = models.CharField(max_length=45, default="")
    Position = models.CharField(max_length=20)
    def __str__(self):
        return self.Faculty_Name


class Issue (models.Model):
    Issue_ID = models.CharField(primary_key=True, max_length=4, default="")
    Issue_Name = models.CharField(max_length=45)
    Issue_Type = models.CharField(max_length=20)
    def __str__(self):
        return self.Issue_Name

class Incident(models.Model):
    Incident_ID = models.CharField(primary_key=True, max_length=4, default="")
    Incident_Type = models.CharField(max_length=45)
    Location = models.CharField(max_length=45)
    Kind_of_Students = models.CharField(max_length=45)
    Group_or_Individual = models.CharField(max_length=20)
    def __str__(self):
        return self.Incident_Type

class Course(models.Model):
    Course_ID = models.CharField(primary_key=True, max_length=10, default="")
    Course_Name = models.CharField(max_length=45)
    Ranking = models.CharField(max_length=2, default="")
    def __str__(self):
        return self.Course_Name

class Request (models.Model):
    Request_ID = models.CharField(primary_key=True, max_length=4, default="")
    Counselor_ID = models.ForeignKey(Student_Advisor_Counselor, on_delete=models.CASCADE)
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Request_Type = models.CharField(max_length=45)
    Time_Appointment = models.DateTimeField(auto_now_add=False)
    Time_Submitted_Appointment = models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.Request_Type


class Student_Issue(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Issue_ID = models.ForeignKey(Issue, on_delete=models.CASCADE)

class Student_Incident(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Incident_ID = models.ForeignKey(Incident, on_delete=models.CASCADE)
    Faculty_ID = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Student_Profile(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
    Credits_Completed = models.CharField(max_length=2, default="")
    Current_Semester = models.CharField(max_length=45)
    Program = models.CharField(max_length=45)
    School = models.CharField(max_length=45)
    Track_Representative = models.CharField(max_length=30, default="")

