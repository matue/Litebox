# Generated by Django 2.0.7 on 2018-07-28 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180728_2323'),
        ('docs', '0003_auto_20180728_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
        migrations.AddField(
            model_name='document',
            name='person',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Person'),
        ),
    ]
