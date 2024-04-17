from django.core.validators import MinValueValidator
from django.db import models

class DonVi(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    Ten = models.CharField(max_length=100, null=False)
    DiaChi = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.Ten
class NhanSu(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    HoDem = models.CharField(max_length=50, null=True)
    Ten = models.CharField(max_length=50, null=False)
    NgaySinh =models.DateTimeField(null=False)
    HeSoLuong = models.FloatField(validators=[MinValueValidator(1.0)], null=False)
    DonViLV = models.ManyToManyField('DONVI', through="NHANSUDONVI")

    def __str__(self):
        return f"{self.HoDem} {self.Ten}"

class NhanSuDonVi(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    NhanSu = models.ForeignKey(NhanSu, on_delete=models.CASCADE, null=False)
    DonVi = models.ForeignKey(DonVi, on_delete=models.CASCADE, null=False)
    VaiTro = models.CharField(max_length=20, null = False, default='Nhân viên')
    DangCongTac = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.NhanSu} - {self.DonVi}"



