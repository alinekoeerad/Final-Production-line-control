# Generated by Django 4.2.4 on 2023-09-10 07:04

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ikco_id', models.CharField(max_length=100)),
                ('technical_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1, null=True)),
                ('reporter', models.CharField(blank=True, max_length=100, null=True)),
                ('expert', models.CharField(blank=True, max_length=100, null=True)),
                ('opinion', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('stopTime', models.TimeField(blank=True)),
                ('samp', models.URLField(blank=True, null=True)),
                ('cReport', models.TextField(blank=True, null=True)),
                ('equip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='color_APP.equip')),
                ('fault', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='color_APP.fault')),
                ('piece', models.ManyToManyField(blank=True, null=True, to='color_APP.piece')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='color_APP.station')),
            ],
        ),
        migrations.AddField(
            model_name='equip',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color_APP.station'),
        ),
    ]
