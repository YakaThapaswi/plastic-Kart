from django.shortcuts import render,HttpResponse,redirect
from home.models import Product
from bag.models import Cart,Cartitem,Whis,Whisitem
from book.models import Address,Order
from members.models import Wallet
import datetime
def add_to_cart(request,id):
    print("hi")
    print(type(id))
    #print(request.name)
    print(id)
    product=Product.objects.get(id=id)
    print(product,request.user)
    cart,_=Cart.objects.get_or_create(user=request.user,ispaid="False")
    obj=Cartitem.objects.filter(cart=cart,product=product)
    print(obj)
    if(obj.exists()):
        print(obj[0].quantity)
        obj.update(quantity=obj[0].quantity+1)
        print(obj[0].quantity)
        #obj.save()
    else:
        cartitem=Cartitem.objects.create(cart=cart,product=product,quantity=1)
        print("not")
    return redirect("/bag/mybag")
def bag(request):

    if Cart.objects.filter(user=request.user).exists():
        prodid=Cartitem.objects.filter(cart=Cart.objects.get(user=request.user))
        if prodid.count()==0:
            return HttpResponse("your cart is empty")
        l=[]
        id=request.session['addrid']
        if(request.method=="POST"):
            print("inpost")
            prize=request.POST.get("place")
            wallet=Wallet.objects.filter(user=request.user)
            amount=wallet[0].amount
            prize=int(prize)
            if(amount>=prize):
                new_amount=amount-prize
                wallet.update(amount=new_amount)
                adr=Address.objects.get(id=id)
                print("sufficient")
                for i in prodid:
                    proditem=Product.objects.get(id=i.product.id)
                    print(proditem)
                    order=Order.objects.create(user=request.user,addressid=adr,status="placed",date=datetime.date.today(),itemid=proditem)
                    order.save()
                return HttpResponse("order placed successfully")
            else:
                return HttpResponse("insufficient balance")
        prize=0
        for i in prodid:
            print(i.quantity)
            proditem=Product.objects.get(id=i.product.id)
            l.append(proditem)
            prize+=((proditem.prize)*i.quantity)
        print(l,prize)
        if id=="":
            detail=""
        else:
            detail=Address.objects.get(id=id)
        print(detail)
        context={"items":l,"tprize":prize,"detail":detail}
        return render(request,"bag.html",context)
           
    else:
        return HttpResponse("your cart is empty")
    '''except:
        return redirect("login")'''
    
def add_to_whis(request,id):
    
    product=Product.objects.get(id=id)
    print(product,request.user)
    whis,_=Whis.objects.get_or_create(user=request.user)
    obj=Whisitem.objects.filter(whis=whis,product=product)
    print(obj)
    if(not obj.exists()):
        whisitem=Whisitem.objects.create(whis=whis,product=product)
        
    return redirect("itemsall")
def whis(request):
    try:
        print(type(request.user))
        if Whis.objects.filter(user=request.user).exists():
            prodid=Whisitem.objects.filter(whis=Whis.objects.get(user=request.user))
            if prodid.count()==0:
                return HttpResponse("your whistlist is empty")
            l=[]
            for i in prodid:
                l.append(Product.objects.get(id=i.product.id))
            print(l)
            context={"items":l}
            print(context)
            return render(request,"whistlist.html",context)

        else:
            return HttpResponse("your whistlist is empty")
    except:
        return redirect("login")
    
def remove_cart_item(request,id):
    cartitem=Cartitem.objects.get(cart=Cart.objects.get(user=request.user),product=Product.objects.get(id=id))
    cartitem.delete()
    return redirect("/bag/mybag")

def remove_whis_item(request,id):
    whisitem=Whisitem.objects.get(whis=Whis.objects.get(user=request.user),product=Product.objects.get(id=id))
    whisitem.delete()
    return redirect("/bag/whistlist/")

def cart_whis(request,id):
    product=Product.objects.get(id=id)
    print(product,request.user)
    whis,_=Whis.objects.get_or_create(user=request.user)
    obj=Whisitem.objects.filter(whis=whis,product=product)
    print(obj)
    if(not obj.exists()):
        whisitem=Whisitem.objects.create(whis=whis,product=product)
    remove_cart_item(request,id)   
    return redirect("/bag/mybag")

def placeorder(request):
    Order.objects.create(user=request.user,)
    obj=Cart.objects.get(user=request.user)
    items=Cartitem.objects.filter(cart=obj)
    items.delete()
    return HttpResponse("your cart is empty")
    '''addressid=models.ForeignKey(Address,on_delete=models.CASCADE,related_name="order")
    status=models.CharField(default="placing",max_length=20)
    date=models.DateField()
    itemid=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order")'''

    '''cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    def __Cart__(self):
        return self.cart'''

    
        



