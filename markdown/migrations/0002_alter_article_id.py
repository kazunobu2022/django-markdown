# Generated by Django 4.2.2 on 2023-06-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
