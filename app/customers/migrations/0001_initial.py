# Generated by Django 4.0.4 on 2023-01-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('age', models.PositiveSmallIntegerField(max_length=3)),
                ('city', models.CharField(max_length=20)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=40)),
                ('business', models.BooleanField()),
            ],
        ),
    ]
