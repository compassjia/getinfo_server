# Generated by Django 2.1.8 on 2021-08-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('sapno', models.CharField(max_length=20)),
                ('serno', models.CharField(max_length=50)),
                ('fundno', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=20)),
                ('ipaddress', models.CharField(max_length=20)),
                ('hostname', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('sys', models.CharField(max_length=50)),
                ('cpuinfo', models.CharField(max_length=50)),
                ('ccmprocess', models.CharField(max_length=20)),
                ('intime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
