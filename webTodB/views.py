from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from saveInfo.models import SaveInfo

def homePage(request):  
        return render(request,"home.html")
def register(request) :
    return render(request,"register.html")
def About_us(request):
    return render(request,"about_us.html") 


def Sign_up(request):
    finalans=0
    try:
        
        if request.method=="POST":   
        
         First_Name=request.POST.get("First_Name")
         Last_Name=request.POST.get("Last_Name")
         Email=request.POST.get("Email")
         Password=request.POST.get("Password")
         finalans=First_Name+Last_Name
         
         en=SaveInfo(First_Name=First_Name,Last_Name=Last_Name,Email=Email,Password=Password)
         en.save()
         
         return HttpResponseRedirect("/register")

    except:
        pass
    return render(request,"sign_up.html")       
