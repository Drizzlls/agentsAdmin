# Generated by Django 4.1.7 on 2023-04-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_agent_iddeal'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='education_n',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
