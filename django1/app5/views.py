from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def doctor1(request):
    return render(request, 'doctor1.html')

def doctor2(request):
    return render(request, 'doctor2.html')

def doctor3(request):
    return render(request, 'doctor3.html')

