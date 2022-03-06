# Generated by Django 3.2.3 on 2021-11-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_num', models.CharField(max_length=9)),
                ('full_name', models.CharField(max_length=40)),
                ('join_time', models.CharField(max_length=45)),
                ('leave_time', models.CharField(max_length=45)),
                ('duration', models.CharField(max_length=45)),
                ('stud_email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'attendance_reg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lect_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('lect_email', models.CharField(max_length=40, unique=True)),
                ('lect_first_name', models.CharField(max_length=45)),
                ('lect_last_name', models.CharField(max_length=45)),
                ('lect_job_title', models.CharField(max_length=45)),
                ('lect_contact', models.CharField(max_length=10, unique=True)),
                ('lect_password', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'lecturer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=40, unique=True)),
                ('course_code', models.CharField(max_length=15)),
                ('lect_id', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'module',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NsfasEmpl',
            fields=[
                ('nsfas_emp_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('n_email', models.CharField(max_length=40, unique=True)),
                ('n_first_name', models.CharField(max_length=45)),
                ('n_last_name', models.CharField(max_length=45)),
                ('n_job_title', models.CharField(max_length=45)),
                ('n_contact', models.CharField(max_length=10, unique=True)),
                ('n_password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'nsfas_empl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NsfasHasStudent',
            fields=[
                ('student_num', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nsfas_emp_id', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'nsfas_has_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('session_link', models.CharField(max_length=500)),
                ('comment', models.TextField(blank=True, null=True)),
                ('module_code', models.CharField(max_length=15)),
                ('posted_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_num', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('stud_email', models.CharField(max_length=40, unique=True)),
                ('stud_first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('stud_last_name', models.CharField(max_length=45)),
                ('nsfas_status', models.CharField(max_length=1)),
                ('course_code', models.CharField(max_length=15)),
                ('stud_password', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentHasModule',
            fields=[
                ('student_num', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('module_code', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'student_has_module',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('student_num', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('stud_password', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'student_login',
                'managed': False,
            },
        ),
    ]
