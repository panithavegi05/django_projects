from django.shortcuts import render # type: ignore

# Create your views here.
from django.shortcuts import render,HttpResponse  # type: ignore
from .models import Student 
def add_student(request): 
    student = Student(name="john doe", age=22, email="johndoe@example.com") 
    student.save() 
    return HttpResponse("Student record added successfully!") 
def student_list(request): 
    students = Student.objects.all() 
    return render(request, 'student.html', {'students': students}) 