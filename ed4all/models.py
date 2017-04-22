from django.db import models
from decimal import Decimal
from django.core.urlresolvers import reverse
from datetime import datetime

class StudentAdvisorCounselor(models.Model):
    counselor_id = models.CharField(db_column='Counselor_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    counselor_name = models.CharField(db_column='Counselor_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Advisor_Counselor'

    def __str__(self):
        return self.counselor_id+"-"+"Counselor ID"

    def get_absolute_url(self):
        return reverse('crud:index')

class Student(models.Model):
    student_id = models.CharField(db_column='Student_ID', primary_key=True,
                                      max_length=8)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45, blank=True,
                                         null=True)  # Field name made lowercase.
    counselor_id = models.CharField(db_column='Counselor_ID', max_length=8, blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
            managed = False
            db_table = 'Student'

    def __str__(self):
        return self.Student_Name

class Faculty(models.Model):
    faculty_id = models.CharField(db_column='Faculty_ID', primary_key=True,
                                      max_length=8)  # Field name made lowercase.
    faculty_name = models.CharField(db_column='Faculty_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45, blank=True,
                                         null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
            managed = False
            db_table = 'Faculty'
    def __str__(self):
        return self.Faculty_Name

class Issue(models.Model):
    issue_id = models.CharField(db_column='Issue_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    issue_name = models.CharField(db_column='Issue_Name', max_length=45)  # Field name made lowercase.
    issue_type = models.CharField(db_column='Issue_Type', max_length=45)  # Field name made lowercase.

    class Meta:
            managed = False
            db_table = 'Issue'

    def __str__(self):
        return self.Issue_Name

class Incident(models.Model):
    Incident_ID = models.CharField(primary_key=True, max_length=8)
    Incident_Type = models.CharField(max_length=45)
    Location = models.CharField(max_length=45)
    Kind_of_Students = models.CharField(max_length=45)
    Group_or_Individual = models.CharField(max_length=20)
    def __str__(self):
        return self.Incident_Type

class Request(models.Model):
    request_id = models.CharField(db_column='Request_ID', primary_key=True,
                                      max_length=8)  # Field name made lowercase.
    request_type = models.CharField(db_column='Request_Type', max_length=45)  # Field name made lowercase.
    time_of_appointment = models.DateTimeField(db_column='Time_of_Appointment')  # Field name made lowercase.
    time_of_submitted_appointment = models.DateTimeField(
            db_column='Time_of_Submitted_Appointment')  # Field name made lowercase.
    student_id = models.IntegerField(db_column='Student_ID')  # Field name made lowercase.
    counselor_id = models.IntegerField(db_column='Counselor_ID')  # Field name made lowercase.

    class Meta:
            managed = False
            db_table = 'Request'

    def __str__(self):
        return self.Request_Type


class StudentIssue(models.Model):
    student_id = models.CharField(db_column='Student_ID', max_length=8)  # Field name made lowercase.
    issue_id = models.CharField(db_column='Issue_ID', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Issue'
        unique_together = (('student_id', 'issue_id'),)

class StudentIncident(models.Model):
    student_id = models.CharField(db_column='Student_ID', max_length=8)  # Field name made lowercase.
    incident_id = models.IntegerField(db_column='Incident_ID')  # Field name made lowercase.
    faculty_id = models.IntegerField(db_column='Faculty_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Incident'
        unique_together = (('student_id', 'incident_id'),)

class StudentProfile(models.Model):
    student_id = models.CharField(db_column='Student_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    gpa = models.DecimalField(db_column='GPA', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    credits_completed = models.CharField(db_column='Credits_Completed', max_length=8, blank=True, null=True)  # Field name made lowercase.
    current_semester = models.CharField(db_column='Current_Semester', max_length=45)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=45)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=45)  # Field name made lowercase.
    track_representitve = models.CharField(db_column='Track_Representitve', max_length=30, blank=True, null=True)  # Field name made lowercase.
    international_or_not = models.CharField(db_column='International_or_not', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Profile'
