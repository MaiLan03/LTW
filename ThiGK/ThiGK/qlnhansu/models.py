from django.db import models


class NHANSU(models.Model):
    id = models.IntegerField(primary_key=True, null=False, db_index=False, )
    HoDem = models.CharField(max_length=50, null=True, )
    Ten = models.CharField(max_length=50, null=False)
    NgaySinh = models.DateTimeField(null=False)
    # HeSoLuong = models.FloatField(min_value =1.0, null=False)
    DonViLV = models.ManyToManyField('DONVI', through="NHANSUDONVI")

    def __str__(self):
        return self.HoDem

class DONVI(models.Model):
    id = models.IntegerField(primary_key=True, null=False, db_index=False)
    Ten = models.CharField(max_length=100, null=False)
    DiaChi = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.Ten


class NHANSUDONVI(models.Model):
    id = models.IntegerField(primary_key=True, null=False, db_index=False)
    NhanSu = models.ForeignKey(NHANSU, on_delete=models.CASCADE, null=False)
    DonVi = models.ForeignKey(DONVI, on_delete=models.CASCADE, null=False)
    VaiTro = models.TextField(max_length=20, null=False, )
    DangCongTac = models.BooleanField()

    def __str__(self):
        return self.NhanSu
