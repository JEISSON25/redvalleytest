# Generated by Django 3.1 on 2021-10-25 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.CharField(choices=[('1', 'CEDULA'), ('2', 'TARJETA DE IDENTIDAD'), ('3', 'CEDULA DE EXTRANJERIA')], max_length=1, verbose_name='Tipo de identificación')),
                ('identiy', models.BigIntegerField(unique=True, verbose_name='Cedula')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Dirección')),
                ('phone_number', models.IntegerField(blank=True, null=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='FollowAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_emis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_emisor', to='account.account')),
                ('accpunt_follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_follow', to='account.account')),
            ],
            options={
                'verbose_name': 'FollowAccount',
                'verbose_name_plural': 'FollowAccount',
            },
        ),
    ]