# Generated by Django 5.0.6 on 2024-06-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='cust_id',
            field=models.PositiveIntegerField(default=8000, unique=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='adhaar_num',
            field=models.CharField(max_length=12),
        ),
    ]
