# Generated by Django 4.1.8 on 2023-08-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_btech_25'),
    ]

    operations = [
        migrations.CreateModel(
            name='pe_se',
            fields=[
                ('hallticket_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
                ('Year_Sem_Branch_Spl_Sec', models.CharField(max_length=50)),
                ('faculty_Name', models.CharField(max_length=50)),
                ('elective', models.CharField(max_length=50)),
            ],
        ),
    ]
