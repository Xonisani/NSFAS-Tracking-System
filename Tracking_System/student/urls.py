from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    
    
    
    url(r'^display_login_details/', views.desplay_stud_login, name = 'display_login_details'),
    
    url(r'^$', views.index, name = 'index'),
    url(r'^home/', views.home, name = 'home'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^lect_login/', views.lect_login, name = 'lect_login'),
    url(r'^lecturer/', views.lecturer, name = 'lecturer'),
    url(r'^stud_login/', views.stud_Login, name = 'stud_Login'),
    url(r'^student/', views.student, name = 'student'),
    url(r'^display_stud_data/', views.display_stud_data, name = 'display_stud_data'),
    url(r'^nsfas/', views.nsfas, name = 'nsfas'),
    url(r'^nsfas_login/', views.nsfas_login, name = 'nsfas_login'),
    url(r'^registration/', views.registration, name = 'registration'),
    path('delete/<int:student_num>',views.delete),
    path('update/<int:student_num>', views.update),
    
   
    
    
]