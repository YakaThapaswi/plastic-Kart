from django.shortcuts import render,HttpResponse,redirect
from book.models import Address,Sell,Order
from members.models import Wallet
from django.contrib.auth.models import auth,User
import datetime
def book(request):
    return render(request,"account.html")
def account(request):
    return render(request,"account.html")
def orders(request):
    allprod=Order.objects.all()
    context={'items':allprod}
    return render(request,'orders.html',context)
def kartwallet(request):
    obj=Wallet.objects.get(user=request.user)
    return render(request,"kartwallet.html",{"amount":obj.amount})
def personalinf(request):
    return render(request,"personalinf.html")
def addbook(request):
    obj=Address.objects.filter(user=request.user)
    context={}
    if(obj.exists()):
        context["details"]=obj
    return render(request,"addressbook.html",context)
def addressbook(request,st):
    if(request.method=="POST"):
        print("working")
        id=request.POST['addr']
        request.session['addrid']=id
        print(id)
        print(request.session['addrid'])
        if(st=="sell"):
            return redirect("sellwaste")
        else:
            return redirect("bag")
    detail=Address.objects.filter(user=request.user)
    return render(request,"addressbook.html",{"details":detail,"st":st})
def payments(request):
    return render(request,"payments.html")
def myaccount(request):
    return render(request,"myaccount.html")
def addaddress(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        area=request.POST.get('area')
        code=request.POST.get('code')
        flat=request.POST.get('flat')
        landmark=request.POST.get('landmark')
        district=request.POST.get('district')
        state=request.POST.get('state')
        Address.objects.create(user=request.user,name=name,mobile=mobile,code=code,district=district,state=state,area=area,flat=flat)
        context={name:name,mobile:mobile,code:code,district:district,state:state,area:area,flat:flat}
        return redirect("addressbook")
    return render(request,"addaddress.html")
def sellwaste(request):
    
    id=request.session['addrid']
    if(request.method=="POST"):
        print("inpost")
        adr=Address.objects.get(id=id)
        ob=Sell.objects.create(user=request.user,addressid=adr,status="placed",date=datetime.date.today())
        ob.save()
        print("created")
        return redirect("sellwaste")
    print(id)
    if id=="":
        detail=""
    else:
        detail=Address.objects.get(id=id)
        print(detail)
    return render(request,"sellwaste.html",{"detail":detail})
    
'''def sellwaste(request):
        print(Sell.objects.filter(user=request.user).exists())
        if Sell.objects.filter(user=request.user).exists():
            adr=Address.objects.get(id=Sell.objects.get(user=request.user,status="placing").addressid.id)
        else:
            adrid=Address.objects.filter(user=request.user)
            if adrid.exists():
                adr=Sell.objects.create(user=request.user,addressid=adrid[0],date=datetime.date.today())
                print(adr)
            else:
                return redirect("addaddress")
        return render(request,"sellwaste.html",{"detail":adr})
        except:
            return redirect("login")'''
        
def services(request):
    item=Sell.objects.filter(status="placed")
    return render(request,"services.html",{"items":item})

def userservice(request,id):
    user=Sell.objects.get(id=id).user
    idr=id
    print(idr)
    if request.method=="POST":
        print("in post")
        amount=request.POST.get('amount')
        
        wallet=Wallet.objects.filter(user=request.user)
        print(wallet)
        print(type(wallet[0].amount))
        new_amount=wallet[0].amount+int(amount)
        wallet.update(amount=new_amount)
        print(amount)
        obj=Sell.objects.filter(id=id)
        obj.update(status="serviced")
        return HttpResponse("successfull")
    context={"user":user,"id":id}
    print(context)
    return render(request,"userservice.html",context)



