
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    
   
    
    url(r'', include('student.urls')),
    url(r'^home/', include('student.urls')),
    url(r'^registration/', include('student.urls')),
    url(r'^login/', include('student.urls')),
    url(r'^lect_login/', include('student.urls')),
    url(r'^lecturer/', include('student.urls')),
    url(r'^nsfas_login/', include('student.urls')),
    url(r'^nsfas/', include('student.urls')),
    url(r'^student_delete/',include('student.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^stud_login', include('student.urls')),
    
]
