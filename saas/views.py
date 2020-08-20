from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User, Tasks
from django.urls import reverse
from django import forms
from django.forms.widgets import DateInput, FileInput
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
# Create your views here.

ACTIVE = 'Active'
SNOOZED = 'Snoozed'
COMPLETED = 'Completed'
CANCELED = 'Canceled'
STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (SNOOZED, 'Snoozed'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class NewTaskForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'class':'form-control'}))
    status = forms.CharField(label='What is the category of the product?', widget=forms.Select(attrs={'class':'form-control'},choices=STATUS_CHOICES))
    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'form-control'}))
    attachment = forms.FileField(required=False, label='Upload a file (optional)', widget=forms.widgets.FileInput(attrs={'class':'form-control'}))

class EditTaskForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'class':'form-control'}))
    status = forms.CharField(label='What is the category of the product?', widget=forms.Select(attrs={'class':'form-control'},choices=STATUS_CHOICES))
    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'form-control'}))
    attachment = forms.FileField(required=False, label='Upload a file (optional)')

def index(request):
    return render(request, "saas/index.html",{
        "tasks": Tasks.objects.filter(user=User(request.user.id),is_completed__exact=False)
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "saas/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "saas/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "saas/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "saas/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def create(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data["content"]
            status = form.cleaned_data["status"]
            deadline = form.cleaned_data["deadline"]
            attachment = request.FILES.get('attachment')

            t = Tasks.objects.create(content=content, user=request.user, status=status, deadline=deadline, attachment=attachment)

            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "saas/create.html", {
                "form": form
            })

    return render(request, "saas/create.html", {
                "form": NewTaskForm()
            })

@login_required
def edit(request, task_id):
    if request.method == "POST":

        form = EditTaskForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data["content"]
            status = form.cleaned_data["status"]
            deadline = form.cleaned_data["deadline"]

            #attachment = form.cleaned_data["attachment"]
            attachment = request.FILES.get('attachment')
            #attachment = request.FILES('attachment')

            t = Tasks.objects.get(id=task_id)
            t.content = content
            t.status = status
            t.deadline = deadline
            if attachment:
                t.attachment = attachment
            t.save()
            
            return HttpResponseRedirect(reverse("index"))
        
    else:
        t = Tasks.objects.get(id=task_id) 
        
        return render(request, "saas/edit.html", {
                "form": EditTaskForm(initial={'content': t.content, 'status':t.status, 'deadline': t.deadline, 'attachment':t.attachment}),
            "task_id":task_id,
            })

@csrf_exempt
def complete(request, task_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            t = Tasks.objects.get(id=task_id)
            t.is_completed = True
            t.save()
        return HttpResponseRedirect(reverse("index"))
        
def download_file(request, file_url):
    path_to_file = file_url
    f = open(path_to_file, 'rb')
    
    response = HttpResponse(f, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+f.name
    return response

def sprint(request, task_id):
    t = Tasks.objects.get(id=task_id)
    return render(request, "saas/sprint.html", {
            "task":t,
    })

def standalone_sprint(request):
    return render(request, "saas/sprint.html", {
            
    })