# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AttendanceReg(models.Model):
    student_num = models.CharField(primary_key=True, max_length=9)
    full_name = models.CharField(max_length=40)
    join_time = models.CharField(max_length=45)
    leave_time = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'attendance_reg'


class Course(models.Model):
    course_code = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'course'


class Lecturer(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=7)
    email = models.CharField(unique=True, max_length=40)
    first_fame = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    job_title = models.CharField(max_length=45)
    phone_num = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lecturer'


class LecturerLogin(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=7)
    password = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'lecturer_login'


class Module(models.Model):
    module_code = models.CharField(primary_key=True, max_length=20)
    module_namel = models.CharField(unique=True, max_length=40)
    course_code = models.CharField(max_length=20)
    lecturer_id = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'module'
        unique_together = (('module_code', 'course_code', 'lecturer_id'),)


class NsfasEmpl(models.Model):
    nsfas_emp_id = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(unique=True, max_length=40)
    first_fame = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    job_title = models.CharField(max_length=45)
    phone_num = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'nsfas_empl'


class NsfasHasStudent(models.Model):
    student_num = models.CharField(primary_key=True, max_length=9)
    nsfas_emp_id = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'nsfas_has_student'
        unique_together = (('student_num', 'nsfas_emp_id'),)


class NsfasLogin(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'nsfas_login'


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_link = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    module_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'session'
        unique_together = (('session_id', 'module_code'),)


class Student(models.Model):
    student_num = models.CharField(primary_key=True, max_length=9)
    stud_email = models.CharField(unique=True, max_length=40)
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=45)
    nsfas_status = models.IntegerField()
    course_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'student'
        unique_together = (('student_num', 'course_code'),)


class StudentHasModule(models.Model):
    student_num = models.CharField(primary_key=True, max_length=9)
    module_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'student_has_module'
        unique_together = (('student_num', 'module_code'),)


class StudentLogin(models.Model):
    student_num = models.CharField(primary_key=True, max_length=9)
    password = models.CharField(unique=True, max_length=20)
    re_password = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'student_login'
