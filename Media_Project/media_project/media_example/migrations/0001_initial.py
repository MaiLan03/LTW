# Generated by Django 4.2.8 on 2024-03-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', models.ImageField(upload_to='images/')),
                ('file_field', models.FileField(upload_to='file/')),
            ],
        ),
    ]
