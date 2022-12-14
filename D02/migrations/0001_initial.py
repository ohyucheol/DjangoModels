# Generated by Django 4.0.6 on 2022-09-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('picture', models.URLField(blank=True)),
                ('space', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('capacity', models.IntegerField(blank=True)),
                ('audio', models.CharField(blank=True, max_length=200)),
                ('video', models.CharField(blank=True, max_length=200)),
                ('other', models.CharField(blank=True, max_length=200)),
                ('information', models.TextField(blank=True, max_length=2000)),
            ],
        ),
    ]
