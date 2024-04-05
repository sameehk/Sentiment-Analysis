import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from sentimentapp.models import *

def userlogin(request):
    return render(request,'user/loginindex.html')

def loginpost(request):
    username = request.POST['textfield']
    passsword = request.POST['textfield2']

    try:
        var = LoginTable.objects.get(username=username,password=passsword)
        if var.type == 'admin':
            return HttpResponse('''<script>alert("Login successfully");window.location="/adminhome"</script>''')
        elif var.type == 'user':
            request.session['lid']=var.id
            return HttpResponse('''<script>alert("Login successfully");window.location="/userhome"</script>''')
    except:

        return HttpResponse('''<script>alert("Invalid login");window.location="/"</script>''')
def regdetails(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['text']
    address=request.POST['textarea2']
    username=request.POST['textfield3']
    password=request.POST['textfield4']
    photo=request.FILES['photo']
    fn=FileSystemStorage()
    fs=fn.save(photo.name,photo)
    ob = LoginTable()
    ob.username = username
    ob.password = password
    ob.type = 'user'
    ob.save()
    uob=Usertable()
    uob.name=name
    uob.phone=phone
    uob.email=email
    uob.address=address
    uob.photo=fs
    uob.LOGIN=ob
    uob.save()
    return HttpResponse('''<script>alert("Registered Successfully");window.location="/"</script>''')

def feedback(request):
    feedback=request.POST['textarea']
    fob=Feedback()
    fob.feedback=feedback
    fob.date=datetime.datetime.today()
    fob.USER=Usertable.objects.get(LOGIN__id=request.session['lid'])
    fob.save()
    return HttpResponse('''<script>alert(" Submitted");window.location="/userhome"</script>''')



def complaint(request):
    complaint=request.POST['text3']
    cob=Complaint()
    cob.complaint=complaint
    cob.USER=Usertable.objects.get(LOGIN__id=request.session['lid'])
    cob.date= datetime.datetime.today()
    cob.reply='pending'
    cob.save()
    return HttpResponse('''<script>alert(" Submitted");window.location="/userhome"</script>''')

def userhome(request):
    return render(request,'user/userindex.html')

def usercomplaint1(request):
    ob = Complaint.objects.all()
    return render(request,'user/usercomplaint1.html',{"val":ob})

def usercomplaint2(request) :
    return render(request,'user/usercomplaint2.html')

def userfeedback(request) :
    return render(request,'user/userfeedback.html')

def register(request) :
    return render(request,'user/register.html')


def adminhome(request):
    return render(request,'admin/adminindex.html')

def adminuserdetails(request) :
    ob = Usertable.objects.all()
    return render(request,'admin/Admin-userdetails.html', {'val': ob})

def blockuser(request,id):
    ob=LoginTable.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert(" Blocked");window.location="/Admin_userdetails"</script>''')

def unblockuser(request,id):
    ob=LoginTable.objects.get(id=id)
    ob.type='user'
    ob.save()
    return HttpResponse('''<script>alert(" Un blocked");window.location="/Admin_userdetails"</script>''')

def admincomplaint(request) :
    ob=Complaint.objects.all()
    return render(request,'admin/admincomplaint.html',{'val':ob})


def searchdate(request):
    date=request.POST['textfield']
    ob=Complaint.objects.filter(date=date)
    return render(request,'admin/admincomplaint.html',{'val':ob})

def feedbacksearchdate(request):
    date=request.POST['textfield']
    ob=Complaint.objects.filter(date=date)
    return render(request,'admin/adminfeedback.html',{'val':ob})

def usercompsearch(request):
    date=request.POST['textfield']
    ob = Complaint.objects.filter(date=date)
    return render(request, 'user/usercomplaint1.html', {'val': ob})


def searchuser(request):
    name=request.POST['textfield']
    ob=Usertable.objects.filter(name=name)
    return render(request,'admin/Admin-userdetails.html',{'val':ob})

def admincomplaintreply(request,id) :
    request.session['pp']=id
    return render(request,'admin/admincomplaintreply.html')

def complaintreply(request):
    reply=request.POST['textfield']
    rob=Complaint.objects.get(id=request.session['pp'])
    rob.reply=reply
    rob.save()
    return HttpResponse('''<script>alert("Reply Sent");window.location="/admincomplaint"</script>''')


def adminfeedback(request) :
    return render(request,'admin/adminfeedback.html')


def insert_review(request) :

    ob=Review()
    ob.product=request.GET['p']
    ob.review=request.GET['r']
    ob.positive=request.GET['po']
    ob.negative=request.GET['ne']
    ob.nuetral=request.GET['nu']
    ob.date=datetime.datetime.today()
    ob.save()
    return HttpResponse("ok")


