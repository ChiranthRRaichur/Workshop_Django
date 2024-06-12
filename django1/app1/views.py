from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import input_form

# Create your views here.

def sqr(request):
    n = int(input("enter a number"))
    res1=fact(n)
    res = n*n
    # res2 = getFact(n)
    return render(request, "app1/index.html", {'n':n, 'res':res, 'res1':res1})

def fact(n):
    facto = 1
    # n = 4
    for i in range(1,n+1):
        facto*=i
    print(facto)
    return facto


def getFact(request):
    factarray= []
    for n in range(1,9):
        # num = n
        fact = 1
        for i in range(1,n+1,1):
            fact*=i
        factarray.append(fact)
    return render(request, "app1/index2.html", {'factarray':factarray})




def home(request):
    if request.method=="POST":
        form1=input_form(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app1/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=input_form()
    return render(request,'app1/index.html',{'form':form1})












    # factorial=[]
    # numbers=[]
    # for j in range(1,n+1,1):
    #     n1=j
    #     fact1=1
    #     for i in range(1,n1+1,1):
    #         fact1=fact1*i
    #     factorial.append(fact1)
    #     numbers.append(n1)
    # return (factorial,numbers)
