from django.shortcuts import render,HttpResponse
#from whistlist.models import Whistlist
def whistlist(request):
    #allprod=Whistlist.objects.all()
    #context={'items':allprod}
    #return render(request,"whistlist.html",context)
    return render(request,"whistlist.html")
def cart(request):
    return render(request,"bag.html")
