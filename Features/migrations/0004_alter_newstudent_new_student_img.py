# Generated by Django 4.0.4 on 2022-05-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Features', '0003_alter_newstudent_new_student_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstudent',
            name='new_student_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]