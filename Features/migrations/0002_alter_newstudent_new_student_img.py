# Generated by Django 4.0.4 on 2022-05-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstudent',
            name='new_student_img',
            field=models.ImageField(blank=True, null=True, upload_to='training_data/'),
        ),
    ]
