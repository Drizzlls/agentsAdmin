# Generated by Django 3.2.9 on 2022-10-16 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0004_agent_iddeal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastName', models.CharField(max_length=50, null=True, verbose_name='Фамилия')),
                ('phone', models.IntegerField(unique=True, verbose_name='Номер телефона')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('agent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='agents.agent', verbose_name='Агент')),
            ],
        ),
    ]
