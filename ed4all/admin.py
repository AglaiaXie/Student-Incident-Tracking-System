from django.contrib import admin
from .models import StudentAdvisorCounselor, Student, Faculty, Issue, Incident, Request, StudentIssue, StudentIncident, StudentProfile

admin.site.register(StudentAdvisorCounselor)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Issue)
admin.site.register(Incident)
admin.site.register(Request)
admin.site.register(StudentIssue)
admin.site.register(StudentIncident)
admin.site.register(StudentProfile)