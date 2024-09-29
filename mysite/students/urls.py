# students/urls.py

from django.urls import path
from . import views
from .views import submit_student, calculate_grades, register, user_login, user_logout
# students/urls.py

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('submit/', views.submit_student, name='submit_student'),
    path('students/', views.student_list, name='student_list'),
    path('grades/', calculate_grades, name='grades'),
    
    
]


