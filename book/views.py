from django.shortcuts import render,HttpResponse
from book.models import Orders
def book(request):
    return render(request,"account.html")
def account(request):
    return render(request,"account.html")
def orders(request):
    allprod=Orders.objects.all()
    context={'items':allprod}
    return render(request,'orders.html',context)
def kartwallet(request):
    return render(request,"kartwallet.html")
def personalinf(request):
    return render(request,"personalinf.html")
def addressbook(request):
    return render(request,"addressbook.html")
def payments(request):
    return render(request,"payments.html")
def myaccount(request):
    return render(request,"myaccount.html")


