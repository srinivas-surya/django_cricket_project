# Generated by Django 3.0.6 on 2020-08-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=20)),
                ('team2', models.CharField(max_length=20)),
                ('winner', models.CharField(max_length=20)),
                ('ccreated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Matches',
                'ordering': ('winner',),
            },
        ),
    ]
