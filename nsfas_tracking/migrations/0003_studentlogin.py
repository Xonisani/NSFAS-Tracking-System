# Generated by Django 3.2.3 on 2021-11-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsfas_tracking', '0002_delete_studentlogin'),
    ]

    operations = [
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
