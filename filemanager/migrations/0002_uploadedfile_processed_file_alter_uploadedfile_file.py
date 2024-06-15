# Generated by Django 4.2.7 on 2024-06-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='processed_file',
            field=models.FileField(blank=True, null=True, upload_to='processed_files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='user_files/%Y/%m/%d'),
        ),
    ]
