# Generated by Django 2.0.7 on 2018-08-21 17:33

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_auto_20180728_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctype',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='document',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='productsindoc',
            name='updated',
        ),
        migrations.AddField(
            model_name='doctype',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='document',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='productsindoc',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='productsindoc',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
    ]
