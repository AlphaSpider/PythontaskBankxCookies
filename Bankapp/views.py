from django.shortcuts import render, HttpResponse, redirect
from .models import Account

# Create your views here.

def home(request):
    print("hello")
    if 'a' in request.session:
        print("jj")
        name = request.session['a']

        user_data=Account.objects.get(uname=name)
        return render(request, "index.html")
    else:
        return redirect("/login")
    
def createacc(request):
    acc_obj=Account()
    if request.method=="POST":
        acc_obj.name=request.POST.get("name")
        acc_obj.adrs=request.POST.get("adrs")
        acc_obj.ph=request.POST.get("ph")
        acc_obj.uname=request.POST.get("uname")
        acc_obj.pswd=request.POST.get("pswd")
        acc_obj.bal=0
        acc_obj.save()
        print(acc_obj)
        return redirect('/')    

    return render(request, "create.html")

def balance(request):
    if 'a' in request.session:
        name = request.session['a']
        acc_obj=Account.objects.get(uname=name)
        acc_bal=acc_obj.bal

        return render(request, "balance.html", {"data": acc_obj})
        # return HttpResponse(acc_bal)

def login(request):
    acc_obj=Account()
    if request.method=="POST":
        i_uname=request.POST.get("uname")
        i_pswd=request.POST.get("pswd")
        # sel_acc=Account.objects.get(uname=i_uname)
        # if i_pswd==sel_acc.pswd:
        user_data = Account.objects.filter(uname=i_uname, pswd=i_pswd)

        if user_data: 
            request.session['a'] = i_uname
            print("Login successful")
            return redirect ('/')
        else:
            return HttpResponse("Invalid username or password")

    return render(request, "login.html")

def deposit(request):
    if 'a' in request.session:
        name=request.session['a']
        user_data=Account.objects.get(uname=name)

        if request.method=="POST":
            amount=float(request.POST.get("amt"))
            acc_bal=user_data.bal
            new_amt=amount+acc_bal
            user_data.bal=new_amt
            user_data.save()
            return redirect('/')
        
        return render(request, "deposit.html")
    
def withdraw(request):
    if 'a' in request.session:
        name=request.session['a']
        acc_obj=Account.objects.get(uname=name)
        b_bal=float(acc_obj.bal)
        if request.method=="POST":
            wd_amt=float(request.POST.get("amt"))
            if wd_amt <= b_bal:
                wd_amt=wd_amt-b_bal
                acc_obj.bal=wd_amt
                acc_obj.save()
            else:
                msg="Insufficient balance!!!"
                return HttpResponse(msg)
            return redirect('/')
    return render(request, "withdrawal.html")



def user_logout(request):

    del request.session['a']
    return redirect('/login')