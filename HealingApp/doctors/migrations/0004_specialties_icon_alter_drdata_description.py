# Generated by Django 5.0.4 on 2024-04-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_openagenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialties',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons'),
        ),
        migrations.AlterField(
            model_name='drdata',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
