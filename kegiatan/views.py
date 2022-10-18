from django.shortcuts import render

# Create your views here.
def kegiatan(request):
    return render(request,'kegiatan.html')