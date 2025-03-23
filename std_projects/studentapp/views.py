from django.shortcuts import render  # type: ignore
def student_list(request): 
    students = [ 
        {'name': 'devi', 'marks': 92}, 
        {'name': 'veni', 'marks': 70}, 
        {'name': 'padma', 'marks': 49}, 
        {'name': 'lakshmi', 'marks': 83}, 
        {'name': 'valli', 'marks': 37}, 
    ] 
    passing_marks = 50  
    return render(request, 'sapp/student_list.html', {'students': students, 'passing_marks': passing_marks})