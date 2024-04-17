# Generated by Django 4.2.8 on 2024-03-12 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DONVI',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Ten', models.CharField(max_length=100)),
                ('DiaChi', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NHANSU',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('HoDem', models.CharField(max_length=50, null=True)),
                ('Ten', models.CharField(max_length=50)),
                ('NgaySinh', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NHANSUDONVI',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('VaiTro', models.TextField(max_length=20)),
                ('DangCongTac', models.BooleanField()),
                ('DonVi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlnhansu.donvi')),
                ('NhanSu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlnhansu.nhansu')),
            ],
        ),
        migrations.AddField(
            model_name='nhansu',
            name='DonViLV',
            field=models.ManyToManyField(through='qlnhansu.NHANSUDONVI', to='qlnhansu.donvi'),
        ),
    ]