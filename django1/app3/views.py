from django.shortcuts import render
from app3.forms import input1_form
from .models import Customers

# global lastnum

# def icici(request):
#     # lastnum = 8000
#     # customer_id = lastnum +1
#     # lastnum+=1
#     # print(customer_id)
#     if request.method == "POST":
#         form1 = input1_form(request.POST)
#         if form1.is_valid():
#             # data=form1.cleaned_data
#             # customer = data.get("customer")
#             form1.save()
#             return render(request,'app3/index.html',{'form1':form1})
#     else:
#         form1 = input1_form()
#     return render(request, 'app3/index.html', {'form1': form1})

# def print_id(request, id):
#     customer1 = get_object_or_404(Customers, id=id)
#     return render(request, "app3/success.html")

def generate_account_number():
    last_customer = Customers.objects.order_by('cust_id').first()
    if last_customer:
        return last_customer.cust_id + 1
    else:
        return 8000

def icici(request):
    if request.method == "POST":
        form1 = input1_form(request.POST)
        if form1.is_valid():
            Customer = form1.save(commit=False)
            Customer.cust_id = generate_account_number()
            Customer.save()
            return render(request, 'app3/index.html', {'form': form1, 'param1': f"Your Customer_ID is: {Customer.cust_id}"})
    else:
        form1 = input1_form()
    return render(request, 'app3/index.html', {'form': form1})