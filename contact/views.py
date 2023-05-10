from django.shortcuts import render,HttpResponse
from contact.models import Contact
def contact(request):
    email=''
    comment=''
    if request.method=="POST":
       email=request.POST.get('email')
       comment=request.POST.get('com')
       print(email,comment)
       ins=Contact(email=email,comment=comment)
       ins.save()
       return HttpResponse("successfull")
    else:
        return render(request,"contacts.html")

