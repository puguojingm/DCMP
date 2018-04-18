from django.shortcuts import render,reverse,redirect,HttpResponse
from django.contrib.auth	import	authenticate,	login,	logout
from django.contrib import messages
from	django.contrib.auth.decorators	import	login_required
# Create your views here.
def dashboard_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not  None :
            #messages.error(request, 'login Success!')
            #login(request)
            return render(request, 'Dashboard/index.html')
        else :
            messages.error(request, 'Invaild login !')
            return render(request, 'Dashboard/login.html')
    elif  request.user.is_authenticated :
        return render(request,'Dashboard/index.html')
    else:
        return render(request, 'Dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    messages.success(request,'logout success')
    return redirect('/dashboard')


@login_required
def index(requset):

    return HttpResponse()
