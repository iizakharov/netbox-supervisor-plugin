# Generated by Django 3.0.5 on 2020-05-08 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenancy', '0009_standardize_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('sid', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField()),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending-configuration', max_length=30)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_', to='tenancy.tenant')),
                ('tenants', models.ManyToManyField(related_name='tenants', to='tenancy.tenant', blank=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'ordering': ['sid'],
            },
        ),
        migrations.CreateModel(
            name='SupervisorTenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='tenants_all', to='netbox_supervisor_plugin.Supervisor')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                related_name='tenant_of',
                                                to='tenancy.tenant')),
            ],
            options={
                'ordering': ['supervisor'],
            },
        ),
    ]
