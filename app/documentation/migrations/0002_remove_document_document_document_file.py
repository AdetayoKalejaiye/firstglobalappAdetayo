# Generated by Django 4.0.4 on 2023-09-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default='', upload_to='documentation/docs'),
            preserve_default=False,
        ),
    ]
