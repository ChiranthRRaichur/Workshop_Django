from django.shortcuts import render
from app2.forms import input_form
# Create your views here.

def home(request):
    if request.method=="POST":
        form1=input_form(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app2/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=input_form()
    return render(request,'app2/index.html',{'form':form1})

