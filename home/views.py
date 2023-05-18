from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from home.models import Product,Variant
def home(request):
    prod=Variant.objects.all()
    context={"items":prod}
    return render(request,"home.html",context)
def productadd(request):
    name=''
    category=''
    image=''
    prize=''
    pr=0 
    subt=''
    if request.method=="POST":
        name=request.POST.get('pname')
        prize=request.POST.get('pcost')
        category=request.POST.get('pcat')
        image=request.POST.get('pimage')
        pr=int(prize)
        subt=request.POST.get('sub')
    #context={'pname':name,'pcost':prize,'pcat':category,'pimage':image}
    ins=Product(name=name,prize=pr,category=category,image=image)
    ins.save()
    #print(name,prize,category,image)
    if subt=="save and next":
        return redirect(product)
    else:
        return HttpResponse("products added successfully")
def product(request):
    return render(request,'prodform.html')
def itemsall(request):
    allprod=Product.objects.all()
    context={'items':allprod}
    return render(request,'itemsall.html',context)
def search(request):
    st=""
    data={}
    if request.method=="POST":
        st=request.POST.get('searching')
        if st!=None:
            d1=Product.objects.filter(category__icontains=st)
            d2=Product.objects.filter(name__icontains=st)
        data={"items":d1|d2}
    return render(request,'search.html',data)
def catsearch(request, cat):
    data=Product.objects.filter(category__icontains=cat)
    print(data)
    prod={"items":data}
    return render(request,'search.html',prod)
def cart(request):
    return render(request,"bag.html")
