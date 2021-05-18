from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import loader
from .models import bloodgroup,login,donerreg,accepterreg,donerstatus,sendrequest

# Create your views here. 

def index(request):
    return render(request,'user/home.html')

def searchaction(request):
    blood=request.POST.get('blood')
    objall = donerreg.objects.filter(bloodgroup=bloodgroup.objects.filter(id=blood))

    objblood=bloodgroup.objects.all()
    context = {"data": objall,"blood":objblood}
    return render(request, 'user/search.html',context)


def search(request):
    objall = donerreg.objects.all()
    objblood=bloodgroup.objects.all()
    context = {"data": objall,"blood":objblood}
    return render(request, 'user/search.html',context)


def sendrequestaction(request,value):
    objrequest=sendrequest()
    objrequest.donerreg=donerreg.objects.get(id=value)
    objrequest.accepterreg=accepterreg.objects.get(login=getsession(request))
    objrequest.requestdate=datetime.date(datetime.now())
    objrequest.save()

    objall = donerreg.objects.all()
    objblood=bloodgroup.objects.all()
    context = {"data": objall,"blood":objblood,"result":"Request is sended"}
    return render(request, 'user/search.html',context)

def viewRequest(request):
    obj1=donerreg.objects.get(login=getsession(request))
    objrequest=sendrequest.objects.filter(donerreg=obj1)
    context = {"data": objrequest}
    return render(request, 'user/viewRequest.html',context)


def updatestatus(request):
    obj = donerstatus.objects.filter(login=getsession(request))
    context = {"data": obj}
    return render(request, 'user/updatestatus.html',context)

def donationstatusaction(request):
    objstatus=donerstatus()
    objstatus.dateofdonation=request.POST.get('dod')
    objstatus.center=request.POST.get('center')
    objstatus.login=getsession(request)
    objstatus.save()
    return updatestatus(request)


def confirm(request,value):
    if value:
        obj=login.objects.get(id=value)
        obj.status=1
        obj.save()
        if obj.user_role =="doner":
            return confirmedDoners(request)
        if obj.user_role == "accepter":
            return confirmedAccepters(request)

def confirmedAccepters(request):
    std = accepterreg.objects.select_related('login').filter(login__user_role="accepter", login__status=1)
    context = {"data": std}
    return render(request, 'administrator/viewAccepterConfirmed.html', context)

def confirmedDoners(request):
    std = donerreg.objects.select_related('login').filter(login__user_role="doner", login__status=1)
    context = {"data": std}
    return render(request, 'administrator/viewDonersConfirmed.html', context)

def viewDonersPending(request):
    std = donerreg.objects.select_related('login').filter(login__user_role="doner", login__status=0)
    context = {"data": std}
    return render(request, 'administrator/viewDonersPending.html', context)

def viewAccepterPending(request):
    std = accepterreg.objects.select_related('login').filter(login__user_role="accepter", login__status=0)
    context = {"data": std}
    return render(request, 'administrator/viewAccepterPending.html', context)


def viewprofile(request):
    if 'lid' in request.session:
        if 'role' in request.session:
            role = request.session['role']
            if role=="doner":
                std=donerreg.objects.filter(login=getsession(request))
            if role=="accepter":
                std=accepterreg.objects.filter(login=getsession(request))
        context = {"data": std,"role":role}
    else:
        return getsession(request)
    return render(request, 'user/viewprofile.html', context)


def loginView(request):
    return render(request, 'user/login.html')

def loginViewAction(request):
    obj = login()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = login.objects.filter(email=username, password=password, status="1")
    if user.count() == 0:
        dic = {'data': 'Invalid user name or password'}
        return render(request,'user/login.html', context=dic)
    else:
        request.session['lid'] = user[0].id
        request.session['role'] = user[0].user_role
        if user[0].user_role == "doner":
            return viewprofile(request)
        elif user[0].user_role == "accepter":
            return viewprofile(request)
        else:
            return viewBlood(request)
    return render(request, 'user/login.html')




def donerReg(request):
    obj = bloodgroup.objects.all()
    context = {"blood": obj}
    return render(request, 'user/donerReg.html',context )

def donerRegaction(request):
    objlogin=login()
    objlogin.user_role="doner"
    objlogin.status=1
    objlogin.email=request.POST.get('email')
    objlogin.password=request.POST.get('password')
    objlogin.save()

    p = login.objects.latest('id')

    objreg=donerreg()
    objreg.name=request.POST.get('name')
    objreg.gender=request.POST.get('gender')
    objreg.address=request.POST.get('address')
    objreg.bloodgroup=bloodgroup.objects.get(id=request.POST.get('blood'))
    objreg.status=0
    objreg.weight=request.POST.get('weight')
    objreg.phone=request.POST.get('phno')
    objreg.dob=request.POST.get('dob')
    objreg.login=p
    objreg.save()
    context = {"data": "Data Inserted"}
    return render(request, 'user/donerReg.html',context)

def accepterReg(request):
    obj = bloodgroup.objects.all()
    context = {"blood": obj}
    return render(request, 'user/accepterReg.html', context)


def accepterRegaction(request):
    objlogin = login()
    objlogin.user_role = "accepter"
    objlogin.status = 1
    objlogin.email = request.POST.get('email')
    objlogin.password = request.POST.get('password')
    objlogin.save()

    p = login.objects.latest('id')

    objreg = accepterreg()
    objreg.name = request.POST.get('name')
    objreg.gender = request.POST.get('gender')
    objreg.address_bio = request.POST.get('address')
    objreg.bloodgroup = bloodgroup.objects.get(id=request.POST.get('blood'))
    objreg.status = 0
    objreg.phone = request.POST.get('phno')
    objreg.login = p
    objreg.save()
    context = {"data": "Data Inserted"}
    return render(request, 'user/accepterReg.html', context)

def addBlood(request):
    return render(request, 'administrator/addBlood.html')

def addBloodaction(request):
    obj=bloodgroup()
    obj.name=request.POST.get('blood')
    obj.save()
    return viewBlood(request)

def viewBlood(request):
    obj=bloodgroup.objects.all()
    context = {"data": obj}
    return render(request, 'administrator/viewBlood.html',context)

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    # if 'lid' in request.session:
    #     return render(request, 'guestuser/pagenotfound.html')
    return render(request, 'user/login.html')

def getsession(request):
    if 'lid' in request.session:
        lid = request.session['lid']
        return login.objects.get(id=lid)
    else:
        dic = {'msg': 'Invalid session'}
        return render(request, 'user/login.html')