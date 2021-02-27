from django.shortcuts import render


# Create your views here.
def rota_padrao(request):
    return render(request, 'default.html')