# Generated by Django 4.2.5 on 2023-10-02 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_delete_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
