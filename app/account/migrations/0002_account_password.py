# Generated by Django 3.1 on 2021-10-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=1, max_length=8, verbose_name='Password'),
            preserve_default=False,
        ),
    ]
