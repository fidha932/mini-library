# Generated by Django 5.1.1 on 2024-09-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0002_delete_librarian'),
    ]

    operations = [
        migrations.CreateModel(
            name='librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
