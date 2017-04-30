from ed4all.models import Appointment, Counselor, Educator, Incident, Student, Studentprofile
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms

# ========== Login and Home Page =========

def counselor_home(request, template_name='ed4all/counselor_home.html'):
    incidents = Incident.objects.all()
    contents = {}
    contents['incidents'] = incidents
    return render(request, template_name, contents)

def student_home(request, template_name='ed4all/student_home.html'):
    profiles = Studentprofile.objects.all()
    contents = {}
    contents['profiles'] = profiles
    return render(request, template_name, contents)

# ========== Forms =========

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CounselorForm(ModelForm):
    class Meta:
        model = Counselor
        fields = '__all__'

class EducatorForm(ModelForm):
        class Meta:
            model = Educator
            fields = '__all__'

class StudentProfileForm(ModelForm):
        class Meta:
            model = Studentprofile
            fields = '__all__'

# =========== counselor view student profile and crud incident ==========

def student_list(request,template_name='ed4all/student_list.html'):
    student = Student.objects.all()
    ctx = {}
    ctx['student'] = student
    return render(request, template_name, ctx)

def student_view(request, pk, template_name='ed4all/student_view.html'):
    student= get_object_or_404(Student, studentid=pk)
    trackrep = get_object_or_404(Student,studentid=student.trackrepid)
    profile = Studentprofile.objects.filter(studentid=pk)
    ctx = {}
    ctx["student"] = student
    ctx["trackrep"] = trackrep
    ctx["profile"] = profile
    return render(request, template_name, ctx)

def incident_list(request,template_name='ed4all/incident_list.html'):
    ctx={}
    incident= Incident.objects.all()
    ctx['incident']=incident
    return render(request,template_name,ctx)

def incident_view(request, pk, template_name='ed4all/incident_view.html'):
    incident= get_object_or_404(Incident, incidentid=pk)
    student = Student.objects.filter(incident=pk)
    counselor=Counselor.objects.filter(incident=pk)
    ctx = {}
    ctx["i"] = incident
    ctx["s"] = student
    ctx['c']=counselor
    return render(request, template_name, ctx)

def incident_edit(request, pk, template_name='ed4all/incident_edit.html'):
    incident= get_object_or_404(Incident, incidentid=pk)
    form = IncidentForm(request.POST or None, instance=incident)
    if form.is_valid():
        form.save()
        return redirect('ed4all:incident_list')
    ctx = {}
    ctx["form"] = form
    ctx["incident"] = incident
    return render(request, template_name, ctx)

def incident_delete(request, pk, template_name='ed4all/incident_delete.html'):
    incident = get_object_or_404(Incident, incidentid=pk)
    if request.method=='POST':
        incident.delete()
        return redirect('ed4all:incident_list')
    ctx = {}
    ctx["incident"] = incident
    return render(request, template_name, ctx)

def incident_create(request, template_name='ed4all/incident_form.html'):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ed4all:counselor_home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


# =========== profile crud ==========

def student_view_detail(request, pk, template_name='ed4all/student_view_detail.html'):
    student= get_object_or_404(Student, studentid=pk)
    trackrep = get_object_or_404(Student,studentid=student.trackRepID)
    profile = Studentprofile.objects.filter(studentid=pk)
    ctx = {}
    ctx["student"] = student
    ctx["trackrep"] = trackrep
    ctx["profile"] = profile
    return render(request, template_name, ctx)