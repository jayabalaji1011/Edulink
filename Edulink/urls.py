from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_profile/',views.student_profile,name='student_profile'),
    path('staff_profile/',views.staff_profile,name='staff_profile'),
     path('student_info/<int:id>/',views.student_info,name='student_info'),
    path('staff_info/<int:id>/',views.staff_info,name='staff_info'),
    path('home/', views.home, name='home'),
    path('student_update/<int:id>/',views.student_update, name='student_update'),
    path('staff_update/<int:id>/',views.staff_update, name='staff_update'),
    path('student_list/',views.student_list,name='student_list'),
    path('staff_list/',views.staff_list,name='staff_list'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('assignment_list/', views.assignment_list, name='assignment_list'),  
    path('student_assignments/', views.student_assignments, name='student_assignments'), 
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

