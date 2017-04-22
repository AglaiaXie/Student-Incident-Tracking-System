# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Faculty(models.Model):
    faculty_id = models.CharField(db_column='Faculty_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    faculty_name = models.CharField(db_column='Faculty_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Faculty'


class Incident(models.Model):
    incident_id = models.CharField(db_column='Incident_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    incident_type = models.CharField(db_column='Incident_Type', max_length=45)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45)  # Field name made lowercase.
    kind_of_students = models.CharField(db_column='Kind_of_Students', max_length=45)  # Field name made lowercase.
    group_or_individual = models.CharField(db_column='Group_or_Individual', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Incident'


class Issue(models.Model):
    issue_id = models.CharField(db_column='Issue_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    issue_name = models.CharField(db_column='Issue_Name', max_length=45)  # Field name made lowercase.
    issue_type = models.CharField(db_column='Issue_Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Issue'


class Request(models.Model):
    request_id = models.CharField(db_column='Request_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    request_type = models.CharField(db_column='Request_Type', max_length=45)  # Field name made lowercase.
    time_of_appointment = models.DateTimeField(db_column='Time_of_Appointment')  # Field name made lowercase.
    time_of_submitted_appointment = models.DateTimeField(db_column='Time_of_Submitted_Appointment')  # Field name made lowercase.
    student_id = models.IntegerField(db_column='Student_ID')  # Field name made lowercase.
    counselor_id = models.IntegerField(db_column='Counselor_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Request'


class Student(models.Model):
    student_id = models.CharField(db_column='Student_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    counselor_id = models.CharField(db_column='Counselor_ID', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'


class StudentAdvisorCounselor(models.Model):
    counselor_id = models.CharField(db_column='Counselor_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    counselor_name = models.CharField(db_column='Counselor_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Advisor_Counselor'


class StudentIncident(models.Model):
    student_id = models.CharField(db_column='Student_ID', max_length=8)  # Field name made lowercase.
    incident_id = models.IntegerField(db_column='Incident_ID')  # Field name made lowercase.
    faculty_id = models.IntegerField(db_column='Faculty_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Incident'
        unique_together = (('student_id', 'incident_id'),)


class StudentIssue(models.Model):
    student_id = models.CharField(db_column='Student_ID', max_length=8)  # Field name made lowercase.
    issue_id = models.CharField(db_column='Issue_ID', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Issue'
        unique_together = (('student_id', 'issue_id'),)


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Ed4AllCourse(models.Model):
    course_id = models.CharField(db_column='Course_ID', max_length=10)  # Field name made lowercase.
    course_name = models.CharField(db_column='Course_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_course'


class Ed4AllFaculty(models.Model):
    faculty_name = models.CharField(db_column='Faculty_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_faculty'


class Ed4AllIncident(models.Model):
    incident_id = models.CharField(db_column='Incident_ID', max_length=10)  # Field name made lowercase.
    incident_type = models.CharField(db_column='Incident_Type', max_length=45)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45)  # Field name made lowercase.
    kind_of_students = models.CharField(db_column='Kind_of_Students', max_length=45)  # Field name made lowercase.
    group_or_individual = models.CharField(db_column='Group_or_Individual', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_incident'


class Ed4AllIssue(models.Model):
    issue_name = models.CharField(db_column='Issue_Name', max_length=45)  # Field name made lowercase.
    issue_type = models.CharField(db_column='Issue_Type', max_length=55)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_issue'


class Ed4AllRequest(models.Model):
    request_type = models.CharField(db_column='Request_Type', max_length=45)  # Field name made lowercase.
    time_appointment = models.DateTimeField(db_column='Time_Appointment')  # Field name made lowercase.
    time_submitted_appointment = models.DateTimeField(db_column='Time_Submitted_Appointment')  # Field name made lowercase.
    counselor_id = models.ForeignKey('Ed4AllStudentAdvisorCounselor', models.DO_NOTHING, db_column='Counselor_ID_id')  # Field name made lowercase.
    student_id = models.ForeignKey('Ed4AllStudent', models.DO_NOTHING, db_column='Student_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_request'


class Ed4AllStudent(models.Model):
    student_name = models.CharField(db_column='Student_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=45)  # Field name made lowercase.
    counselor_id = models.ForeignKey('Ed4AllStudentAdvisorCounselor', models.DO_NOTHING, db_column='Counselor_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_student'


class Ed4AllStudentAdvisorCounselor(models.Model):
    counselor_name = models.CharField(db_column='Counselor_Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=55)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_student_advisor_counselor'


class Ed4AllStudentIncident(models.Model):
    faculty_id = models.ForeignKey(Ed4AllFaculty, models.DO_NOTHING, db_column='Faculty_ID_id')  # Field name made lowercase.
    incident_id = models.ForeignKey(Ed4AllIncident, models.DO_NOTHING, db_column='Incident_ID_id')  # Field name made lowercase.
    student_id = models.ForeignKey(Ed4AllStudent, models.DO_NOTHING, db_column='Student_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_student_incident'


class Ed4AllStudentIssue(models.Model):
    issue_id = models.ForeignKey(Ed4AllIssue, models.DO_NOTHING, db_column='Issue_ID_id')  # Field name made lowercase.
    student_id = models.ForeignKey(Ed4AllStudent, models.DO_NOTHING, db_column='Student_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_student_issue'


class Ed4AllStudentProfile(models.Model):
    gpa = models.DecimalField(db_column='GPA', max_digits=3, decimal_places=2)  # Field name made lowercase.
    current_semester = models.CharField(db_column='Current_Semester', max_length=45)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=45)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=45)  # Field name made lowercase.
    student_id = models.ForeignKey(Ed4AllStudent, models.DO_NOTHING, db_column='Student_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ed4all_student_profile'
