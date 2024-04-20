# Generated by Django 5.0.4 on 2024-04-19 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patients.appointment')),
            ],
        ),
    ]
