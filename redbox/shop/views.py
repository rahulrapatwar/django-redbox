from django.shortcuts import render

# Create your views here.
def games(request):
    return render(request,'shop/store.html')

def movies(request):
    return render(request,'shop/store.html')
