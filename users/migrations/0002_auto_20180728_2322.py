# Generated by Django 2.0.7 on 2018-07-28 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user_id',
            new_name='user',
        ),
    ]
