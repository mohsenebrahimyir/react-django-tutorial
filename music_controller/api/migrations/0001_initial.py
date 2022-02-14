# Generated by Django 3.2 on 2022-02-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=8, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('guest_can_pause', models.BooleanField(default=False, null=True)),
                ('votes_to_skip', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
