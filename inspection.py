# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Appointment(models.Model):
    appointmentid = models.AutoField(db_column='appointmentID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID_id', blank=True, null=True)  # Field name made lowercase.
    counselorid = models.ForeignKey('Counselor', models.DO_NOTHING, db_column='counselorID_id', blank=True, null=True)  # Field name made lowercase.
    astarttime = models.DateTimeField(db_column='aStartTime', blank=True, null=True)  # Field name made lowercase.
    aendtime = models.DateTimeField(db_column='aEndTime', blank=True, null=True)  # Field name made lowercase.
    requestcomment = models.CharField(db_column='requestComment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    requesttype = models.CharField(db_column='requestType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    timeofsubmittingrequest = models.DateTimeField(db_column='timeOfSubmittingRequest', blank=True, null=True)  # Field name made lowercase.
    requeststarttime = models.DateTimeField(db_column='requestStartTime', blank=True, null=True)  # Field name made lowercase.
    requestendtime = models.DateTimeField(db_column='requestEndTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class Counselor(models.Model):
    counselorid = models.CharField(db_column='counselorID', primary_key=True, max_length=10)  # Field name made lowercase.
    counselorlname = models.CharField(db_column='counselorLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    counselorfname = models.CharField(db_column='counselorFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    counselorpassword = models.CharField(db_column='counselorPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'counselor'


class Educator(models.Model):
    educatorid = models.CharField(db_column='educatorID', primary_key=True, max_length=10)  # Field name made lowercase.
    educatorlname = models.CharField(db_column='educatorLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatorfname = models.CharField(db_column='educatorFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatortype = models.CharField(db_column='educatorType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    educatoremailaddress = models.CharField(db_column='educatorEmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatorpassword = models.CharField(db_column='educatorPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'educator'


class Incident(models.Model):
    incidentid = models.AutoField(db_column='incidentID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID_id', blank=True, null=True)  # Field name made lowercase.
    incidenttype = models.CharField(db_column='incidentType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)
    educatorid = models.ForeignKey(Educator, models.DO_NOTHING, db_column='educatorID_id', blank=True, null=True)  # Field name made lowercase.
    counselorid = models.ForeignKey(Counselor, models.DO_NOTHING, db_column='counselorID_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incident'


class Student(models.Model):
    studentid = models.CharField(db_column='studentID', primary_key=True, max_length=10)  # Field name made lowercase.
    studentlname = models.CharField(db_column='studentLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studentfname = models.CharField(db_column='studentFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studentemailaddress = models.CharField(db_column='studentEmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studentage = models.IntegerField(db_column='studentAge', blank=True, null=True)  # Field name made lowercase.
    studentdob = models.DateField(db_column='studentDOB', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    program = models.CharField(max_length=30, blank=True, null=True)
    trackrepid = models.ForeignKey('self', models.DO_NOTHING, db_column='trackRepID', blank=True, null=True)  # Field name made lowercase.
    studentpassword = models.CharField(db_column='studentPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studenttype = models.CharField(db_column='studentType', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Studentprofile(models.Model):
    profileid = models.CharField(db_column='profileID', primary_key=True, max_length=10)  # Field name made lowercase.
    category = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    seq = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentID', blank=True, null=True)  # Field name made lowercase.
    studentprofilecol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentprofile'
