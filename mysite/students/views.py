import csv
import pandas as pd 
from django.shortcuts import render,redirect
# students/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'students/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'students/login.html')

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
def home(request):
    return HttpResponse("Welcome to the Home Page")
    return render(request, 'students/home.html')
# students/views.py
def submit_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
            # Save to database
            Student.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                bio=form.cleaned_data['bio']
            )
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'students/submit.html', {'form': form})
#calculation
'''def calculate_grades(request):
    students_data = []
    total_grade = 0
    highest_grade = 0
    highest_student = ""

    # Read CSV file
    with open('students.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            age = int(row['age'])
            grade = float(row['grade'])
            total_grade += grade

            # Check for highest grade
            if grade > highest_grade:
                highest_grade = grade
                highest_student = name
            
            students_data.append({'name': name, 'age': age, 'grade': grade})

    average_grade = total_grade / len(students_data) if students_data else 0

    context = {
        'students': students_data,
        'average_grade': average_grade,
        'highest_student': highest_student,
        'highest_grade': highest_grade,
    }
    return render(request, 'students/grades.html', context)'''
def calculate_grades(request):
    csv_file_path = r'C:\Users\sushma suddala\Desktop\mysite\students_record.csv'

    grades = []
    try:
        df = pd.read_csv(csv_file_path, encoding='ISO-8859-1',on_bad_lines='skip')  # Try changing encoding here as needed
        print(df.head())
        if 'grade' in df.columns:
            grades = df['grade'].astype(float).tolist()  # Convert grades to float
        else:
            return HttpResponse("Column 'grade' not found in CSV file.")
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}")

    average_grade = sum(grades) / len(grades) if grades else 0
    highest_grade = max(grades) if grades else None

    context = {
        'average_grade': average_grade,
        'highest_grade': highest_grade,
        'grades': grades
    }

    return render(request, 'students/grades.html', context)

def student_list(request):
    students = Student.objects.all()  # Get all students from the database
    return render(request, 'students/student_list.html', {'students': students})
def home(request):
    return redirect('submit_student')
