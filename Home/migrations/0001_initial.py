# Generated by Django 5.1.1 on 2024-09-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='robo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('like', models.IntegerField()),
                ('comment', models.IntegerField()),
                ('share', models.IntegerField()),
                ('about', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
