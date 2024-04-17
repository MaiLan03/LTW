from django.contrib import messages
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect

from .form import NhanSuForm
from .models import NHANSU, DONVI, NHANSUDONVI


def nhansu(request):
 return render(request, 'base.html')

def nhansu1(request):
 return render(request, 'dsnhansu.html')
def dsnhansu(request):
    ids = NHANSU.objects.all()
    danhsachNS = []
    for id in ids:
        id = id.review_set.all()
        HoDem= None
        Ten = None
        NgaySinh=None
        HeSoLuong=None
        DonViLV =None
        danhsachNS.append(
            {
                "ID": id,
                "Ho_Dem": HoDem,
                "Ten": Ten,
                "NgaySinh": NgaySinh,
                "HeSoLuong": HeSoLuong,
                "DonViLV": DonViLV,
            }
        )
        context = {"danhsachNS": danhsachNS}
        return render(request,'dsnhansu.html',context)

def suanhansu(request,pk=None):
    if pk is not None:
        nhansu = get_object_or_404(NHANSU, pk=pk)
    else:
        nhansu = None
    if request.method == "POST":
        form = NhanSuForm(request.POST, instance=nhansu)
        if form.is_valid():
            updated_nhansu = form.save()
            if nhansu is None:
                messages.success(request, f"NhanSu {updated_nhansu} was created.")
            else:
                messages.success(request, f"NhanSu {updated_nhansu} was updated.")
            return redirect("suanhansu", pk=updated_nhansu.pk)
    else:
        form = NhanSuForm(instance=nhansu)
    return render(
        request,
        "suanhansu.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "NHANSU",
            "instance": nhansu,
        },
    )

