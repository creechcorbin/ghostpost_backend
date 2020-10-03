# Generated by Django 3.1.1 on 2020-09-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('post_time', models.DateTimeField()),
            ],
            options={
                'ordering': ['-post_time'],
            },
        ),
        migrations.CreateModel(
            name='Roast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('post_time', models.DateTimeField()),
            ],
            options={
                'ordering': ['-post_time'],
            },
        ),
    ]
