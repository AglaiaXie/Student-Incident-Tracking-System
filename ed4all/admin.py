from django.contrib import admin
from .models import Student_Advisor_Counselor, Student, Faculty, Issue, Incident, Course, Request, Student_Issue, Student_Incident, Student_Profile

admin.site.register(Student_Advisor_Counselor)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Issue)
admin.site.register(Incident)
admin.site.register(Course)
admin.site.register(Request)
admin.site.register(Student_Issue)
admin.site.register(Student_Incident)
admin.site.register(Student_Profile)