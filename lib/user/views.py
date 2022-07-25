from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def dashboard(request):
   return render(request,"index.html")     
 
#================================================================

def login_user(request):
   if request.method =='POST':
      user = authenticate(
         request,
         username=request.POST['username'],
         password=request.POST['password'],
      )
      if user is not None:
         login(request,user)
         return redirect('')
      else:
         return redirect("login/")
   else:
       return render(request,'login.html')




# ========================================================



def register_user(request):
   if request.method=='POST':
      User.objects.create_user(
         first_name = request.POST['firstname'],
         last_name = request.POST['lastname'],
         username = request.POST['username'],
         password = request.POST['password']
      )
      return redirect("/login")
   else:
      return render(request,'registration.html')


# ===================================================================

def user_about(request):
   return render(request,"about.html")


def user_product(request):
   return render(request,'product.html')


