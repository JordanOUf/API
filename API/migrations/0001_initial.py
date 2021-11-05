# Generated by Django 3.2.8 on 2021-11-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('fb_id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('score_value', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
