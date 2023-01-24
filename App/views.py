from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponse
from App.forms import *
# Create your views here.

class CBV_Form(FormView):
    template_name='CBV_Form.html'
    form_class=NameForm

    def form_valid(self, form):
        return HttpResponse(str(form.cleaned_data))
    

class CBV_ModelForm(FormView):
    template_name='CBV_ModelForm.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data inserted Successfully')