# Generated by Django 2.2.2 on 2020-02-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('a1', models.CharField(max_length=200)),
                ('a2', models.CharField(max_length=200)),
                ('a3', models.CharField(max_length=200)),
                ('a4', models.CharField(max_length=200)),
                ('c', models.IntegerField()),
            ],
        ),
    ]
