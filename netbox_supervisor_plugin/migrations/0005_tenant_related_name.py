# Generated by Django 3.1 on 2020-10-29 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0011_standardize_name_length'),
        ('netbox_supervisor_plugin', '0004_changelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisortenant',
            name='tenant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                       related_name='supervisor',
                                       to='tenancy.tenant'),
        ),
    ]
