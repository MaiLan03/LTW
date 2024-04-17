from django.shortcuts import render

from .models import NhanSu

def dsnhansu(request):
    nhansu_list = NhanSu.objects.all()
    return render(request, 'dsnhansu.html', {'nhansu_list': nhansu_list})
