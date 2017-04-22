from .models import Student, StudentAdvisorCounselor, StudentProfile, StudentIncident, StudentIssue, Faculty, Issue, Incident, Request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request,'ed4all/index.html')

class CounselorCreate(CreateView):
    model = StudentAdvisorCounselor
    fields = ['counselor_id','counselor_name', 'email_address']
    template_name = 'ed4all/counselor_form.html'
    success_url = reverse_lazy('ed4all:index')

class CounselorRead(ListView):
    model = StudentAdvisorCounselor
    template_name = 'ed4all/counselor_list.html'
    #def get_queryset(self):
       # return StudentAdvisorCounselor.objects.all()

class CounselorUpdate(UpdateView):
    model = StudentAdvisorCounselor
    success_url = reverse_lazy('ed4all:view-counselor')
    fields = ['counselor_id','counselor_name', 'email_address']
    template_name = 'ed4all/counselor_update.html'

class CounselorDelete(DeleteView):
    model = StudentAdvisorCounselor
    success_url = reverse_lazy('ed4all:view-counselor')
    template_name = 'ed4all/counselor_confirm_delete.html'

