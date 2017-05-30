from django.shortcuts import render,redirect
from .models import Course, Description

def index(request):
    context = {
    "courses" : Course.objects.all(),
    "descriptions" : Description.objects.all(),
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    course = Course.objects.create(name=request.POST['name'])
    description = Description.objects.create(name=request.POST['description'], course=course)
    print "just added", course.id,description.id
    return redirect('/')

def confirmdelete(request, id):
    course = Course.objects.get(id=id)
    context = {
    "deleted" : course
    }

    return render(request, 'courses_app/confirmdelete.html', context)


def delete(request):
    id = request.POST['id']
    print id
    course = Course.objects.get(id = id).delete()
    return redirect('/')
