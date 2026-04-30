from django.shortcuts import render, redirect
from .models import dept as DeptModel
from .models import Doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def contact(request):
    return render(request, 'contact.html')


@login_required
def department_view(request):
    dict_dept = {
        'dept': DeptModel.objects.all()
    }
    return render(request, 'department.html', dict_dept)


@login_required
def doctors(request):
    dict_docs = {
        'doctors': Doctor.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookingForm()              

    return render(request, 'booking.html', {'form': form})


