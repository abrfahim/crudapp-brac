from django.shortcuts import render, redirect
from . models import Employee
import os

# Create your views here.
    


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        
        if image:
            employee = Employee.objects.create(name=name, email=email, age=age, gender=gender, image=image, address=address)
            employee.save()
        else:
            employee = Employee.objects.create(name=name, email=email, age=age, gender=gender, address=address)
            employee.save()
            
        
    return render(request, 'index.html')


def all_profile(request):
    employee = Employee.objects.all()
    return render(request, 'person/all_profile.html', locals())


def delete_profile(request, id):
    profile = Employee.objects.get(id=id)
    if profile.image != 'default_human.jpg':
        os.remove(profile.image.path)
    profile.delete()
    return redirect('person:all_profile')


def update_profile(request,id):
    profile = Employee.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        
        if image:
            profile.name = name
            profile.email = email
            profile.age = age
            profile.gender = gender
            
            if profile.image != 'default_human.jpg':
                os.remove(profile.image.path)
                profile.delete()
            
            profile.image = image
            profile.address = address
            profile.save()
            return redirect('person:all_profile')
            
        else:
            profile.name = name
            profile.email = email
            profile.age = age
            profile.gender = gender
            profile.address = address
            profile.save()
            return redirect('person:all_profile')
        
    return render(request, 'person/update_profile.html', locals())
    