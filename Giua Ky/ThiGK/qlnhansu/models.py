from django.db import models

class DonVi(models.Model):
    Ten = models.CharField(max_length=100)
    DiaChi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Ten

class NhanSu(models.Model):
    objects = None
    HoDem = models.CharField(max_length=50, blank=True, null=True)
    Ten = models.CharField(max_length=50)
    NgaySinh = models.DateField()
    HeSoLuong = models.FloatField(default=1.0)
    DonViLV = models.ManyToManyField(DonVi, through='NhanSuDonVi')

    def __str__(self):
        return f"{self.HoDem} {self.Ten}"

class NhanSuDonVi(models.Model):
    VAI_TRO_CHOICES = [
        ('Nhân viên', 'Nhân viên'),
        ('Quản lý', 'Quản lý'),
    ]
    nhan_su = models.ForeignKey(NhanSu, on_delete=models.CASCADE)
    don_vi = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    VaiTro = models.CharField(max_length=20, choices=VAI_TRO_CHOICES, default='Nhân viên')
    DangCongTac = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nhan_su} - {self.don_vi}"

from django import forms
from .models import NhanSu

class NhanSuForm(forms.ModelForm):
    class Meta:
        model = NhanSu
        fields = '__all__'  # Hoặc có thể chỉ định các trường cần thiết
