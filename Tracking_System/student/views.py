from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import mysql.connector
from django.contrib import messages
from operator import itemgetter
from .models import *
from .forms import RegistrationForm, UpdateForm

def registration2(request):

    if request.method=='POST':
        if request.POST.get('student_num') and request.POST.get('password') and request.POST.get('repassword'):
            stud = StudentLogin()

            stud.student_num=request.POST.get('student_num')
            stud.password=request.POST.get('password')
            stud.re_password=request.POST.get('repassword')
            stud.save()
            messages.success(request, "Your are successfully registered")
            return render(request, 'new_registration.html')
    else:
        return render(request, 'registration.html')
    return render(request, 'registration.html')

def index(request):

    return render(request, 'index.html')

def home(request):

    return render(request, 'home.html')

def stud_Login(request):

    con = mysql.connector.connect(host="127.0.0.1", user = "root", passwd = "1234", database = "school")
    cursor = con.cursor()

    con2 = mysql.connector.connect(host="127.0.0.1", user = "root", passwd = "1234", database = "school")
    cursor2 = con2.cursor()

    sqlcommand = "select student_num from student_login"
    sqlcommand2 = "select password from student_login"

    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    student_num = []
    passcodes = []

    for i in cursor:
        student_num.append(i)
    for x in cursor2:
        passcodes.append(x)
    print(student_num)
    print(passcodes)

    all_Student_num = list(map(itemgetter(0), student_num))
    all_passcodes = list(map(itemgetter(0), passcodes))


    if request.method=="POST":
        stud_num = request.POST['student_num']
        passward = request.POST['password']
        
        k = len(student_num)
        for i in range(k):
            if all_passcodes[i]==passward and all_Student_num[i] == stud_num:
                return render(request, 'student.html')
                break
        
        else:
            messages.info(request, 'Please enter the correct student number or password')
            return render(request, 'stud_Login.html')
            
    return render(request, 'stud_Login.html')

def student(request):

    return stud_Login(request)

def registration(request):

    stud = Student()

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "You are successfully registered")
    else:
        messages.success(request, "Only NSFAS funded student can register to the system")

    return render(request, 'new_registration.html')

def lect_login(request):
    con = mysql.connector.connect(host="127.0.0.1", user = "root", passwd = "1234", database = "school")
    cursor = con.cursor()

    con2 = mysql.connector.connect(host="127.0.0.1", user = "root", passwd = "1234", database = "school")
    cursor2 = con2.cursor()

    sqlcommand = "select emp_id from lecturer_login"
    sqlcommand2 = "select password from lecturer_login"

    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    emp_id = []
    passcodes = []

    for i in cursor:
        emp_id.append(i)
    for x in cursor2:
        passcodes.append(x)
    print(emp_id)
    print(passcodes)

    all_Lect_id = list(map(itemgetter(0), emp_id))
    all_passcodes = list(map(itemgetter(0), passcodes))


    if request.method=="POST":
        lecturer_id = request.POST['lecturer_id']
        passward = request.POST['password']
        
        k = len(emp_id)
        for i in range(k):
            if all_passcodes[i]==passward and all_Lect_id[i] == lecturer_id:
                return render(request, 'lecturer.html')
                break
        
        else:
            messages.info(request, 'Please enter the correct email or password')
            return render(request, 'lecturer_login.html')

    return render(request, 'lecturer_login.html')

def lecturer(request):
    return render(request,  'lecturer.html')

def nsfas(request):
    return render(request, 'nsfas.html')

def nsfas_login(request):
    con = mysql.connector.connect(host="127.0.0.1", user = "root", passwd = "1234", database = "school")
    cursor = con.cursor()

    con2 = mysql.connector.connect(host="127.0.0.1", user = "root", passwd = "1234", database = "school")
    cursor2 = con2.cursor()

    sqlcommand = "select emp_id from nsfas_login"
    sqlcommand2 = "select password from nsfas_login"

    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    empl_id = []
    passcodes = []

    for i in cursor:
        empl_id.append(i)
    for x in cursor2:
        passcodes.append(x)
    print(empl_id)
    print(passcodes)

    all_nsfas_id = list(map(itemgetter(0), empl_id))
    all_passcodes = list(map(itemgetter(0), passcodes))


    if request.method=="POST":
        emp_id = request.POST['emp_id']
        passward = request.POST['password']
        
        k = len(empl_id)
        for i in range(k):
            if all_passcodes[i]==passward and all_nsfas_id[i] == emp_id:
                
                attend = AttendanceReg.objects.all()
                
                return render(request, 'nsfas.html', {'attend': attend})
                break
        
        else:
            messages.info(request, 'Please enter the correct employee_ID or password')
            return render(request, 'nsfas_login.html')

    return render(request, 'nsfas_login.html')

def login(request):

    return render(request, 'login.html')

def desplay_stud_login(request):
    stud_login = StudentLogin.objects.all()
    context = {'stud_login': stud_login}

    return render(request, 'display_login_details.html', context)
    

def delete(request,student_num):

    stud_login = StudentLogin.objects.get(pk=student_num)
    stud_login.delete()
    return redirect('display_login_details')

def display_stud_data(request):
    stud = Student.objects.all()
    return render(request, 'display_stud_details.html', {'stud':stud})

def update(request, student_num):
    stud = Student.objects.get(pk=student_num)
    form = UpdateForm(request.POST, instance=stud)
    if form.is_valid():
        form.save()
        messages.success(request, "The record is successfully updated")    
    return render(request,'update.html', {'stud':stud})
##########################################################################################
