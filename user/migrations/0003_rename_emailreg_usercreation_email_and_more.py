# Generated by Django 4.1 on 2022-10-04 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usercreation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercreation',
            old_name='emailReg',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usercreation',
            old_name='usernameReg',
            new_name='username',
        ),
    ]
