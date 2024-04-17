from django.shortcuts import render
from .models import NhanSu

def dsnhansu(request):
    danh_sach_nhan_su = NhanSu.objects.all()
    return render(request, 'dsnhansu.html', {'danh_sach_nhan_su': danh_sach_nhan_su})
