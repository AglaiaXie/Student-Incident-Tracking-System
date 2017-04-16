from django.http import HttpResponse
from .models import Student, Student_Advisor_Counselor, Student_Profile, Student_Incident, Student_Issue, Course, Faculty, Issue, Incident, Request

def index(request):
    return HttpResponse("<h1> Education4 <h1>")

