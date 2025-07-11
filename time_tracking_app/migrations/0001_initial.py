# Generated by Django 5.2.4 on 2025-07-09 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StaffName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField(default=None, null=True)),
                ('comment', models.TextField(blank=True, default='')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_tracking_app.project')),
                ('staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_tracking_app.staffname')),
            ],
        ),
    ]
