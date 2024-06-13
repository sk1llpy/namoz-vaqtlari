from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def tasbih(request):
    return render(request, 'tasbih.html')