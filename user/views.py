from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['passwordReg1']
        password2 = request.POST['passwordReg2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error('Bu email kullanılmıştır')
                return redirect('login')
            elif '!' in username or '?' in username or '.' in username:
                messages.error('İsimde özel ? . ! gibi özel karakterler kullanılamaz')
                return redirect('login')
            else:
                user = User.objects.create_user(username = username, email = email, password = password1)
                UserCreation.objects.create(
                    user = user,
                    username = username,
                    email = email



                    
                )
                user.save()
                messages.success(request, 'kullanıcı oluşturuldu')
                return redirect('login')
    return render(request, 'register.html')



def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla Giriş Yaptınız')
            return redirect('index')
                    
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'login.html')


def userLogout(request):
    logout(request)
    return redirect('index')




# def userLogin(request):
#     if request.method == "POST":
#         if request.POST.get('submit') == 'sign_in':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username = username, password = password)

#             if user is not None:
#                 login(request, user)
#                 messages.sucess(request, 'Başarıyla Giriş Yaptınız')
#                 return redirect('index')
#             else:
#                 messages.error(request,'Kullanıcı adı veya şifre hatalı')
#                 return redirect('login')
       
#         elif request.POST.get('submit') == 'sign_up':
#             username = request.POST['username']
#             email = request.POST['email']
#             password1 = request.POST['passwordReg1']
#             password2 = request.POST['passwordReg2']

#             if password1 == password2:
#                 if User.objects.filter(email=email).exists():
#                     messages.error('Bu email kullanılmıştır')
#                     return redirect('login')
#                 elif (password1.len < 6):
#                     messages.error('Şifreniz 6 karakterden uzun olmalıdır')
#                     return redirect('login')
#                 elif '!' in username or '?' in username or '.' in username:
#                     messages.error('İsimde özel ? . ! gibi özel karakterler kullanılamaz')
#                     return redirect('login')
#                 else:
#                     user = User.objects.create(username = email, email = email, password = password1)
#                     UserCreation.objects.create(
#                     user = user,
#                     username = username,
#                     email = email
#                     )
#                     user.save()
#                     messages.success(request, 'kullanıcı oluşturuldu')
#                     return redirect('login')
#     return render(request, 'login.html')        

