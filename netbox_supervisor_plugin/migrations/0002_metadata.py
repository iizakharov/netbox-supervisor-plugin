# Generated by Django 3.0.6 on 2020-07-21 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_supervisor_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supervisor',
            options={'ordering': ['sid'], 'verbose_name': 'Ответственный', 'verbose_name_plural': 'Ответственные'},
        ),
        migrations.AlterModelOptions(
            name='supervisortenant',
            options={'ordering': ['supervisor'], 'verbose_name': 'Связь учреждения и ответственного', 'verbose_name_plural': 'Связи учреждения и ответственного'},
        ),
    ]
