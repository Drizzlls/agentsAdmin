# Generated by Django 4.1.2 on 2022-10-12 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Managers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('idFromBitrix', models.IntegerField(unique=True)),
                ('education', models.BooleanField(blank=True, default=False)),
                ('personalManager', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='Managers.manager')),
            ],
        ),
    ]
