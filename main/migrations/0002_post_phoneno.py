# Generated by Django 4.0.5 on 2022-09-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phoneno',
            field=models.CharField(default='phone number', max_length=13, null=True),
        ),
    ]
