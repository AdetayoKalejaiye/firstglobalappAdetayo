# Generated by Django 4.0.4 on 2023-09-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0002_remove_document_document_document_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['name']},
        ),
    ]
