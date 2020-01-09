from django.shortcuts import render
from attapp.models import student,faculty,admin,marks,sattendance,studentleave,facultyleave
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
def display(request):
    if request.method=='POST':
        studentid=request.POST.get('studentid')
        username=request.POST.get('username')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        admissiondate=request.POST.get('admissiondate')
        mobileno=request.POST.get('mobileno')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        password=request.POST.get('password')
        a=student(studentid=studentid,username=username,address=address,gender=gender,dob=dob,email=email,admissiondate=admissiondate,mobileno=mobileno, guardian= guardian, batch=batch,password=password)
        a.save()
    return render(request,'login.html')


def fsignup(request):
    if request.method=='POST':
        facultyid=request.POST.get('facultyid')
        username=request.POST.get('username')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        batchincharge=request.POST.get('batchincharge')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        password=request.POST.get('password')
        b=faculty(facultyid=facultyid,username=username,address=address,gender=gender,dob=dob,email=email,qualification=qualification,mobileno=mobileno, batchincharge=batchincharge,password=password)
        b.save()
    return render(request,'login.html')



def authentication(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username,password=password)
        if u.count()==1:
            return render(request,'adminhome.html')
        else:
             u1=faculty.objects.filter(username=username,password=password)
             if u1.count()==1:
                 request.session['usrname']=username
                 return render(request,'facultyhome.html')
             else:
               u2=student.objects.filter(username=username,password=password)      
               if u2.count()==1:
                 request.session['usrname']=username
                 return render(request,'studenthome.html')
               else:
                 return HttpResponse('login unsuccesfull')  
def viewfacpro(request):
     queryset=faculty.objects.all().filter(username=request.session['usrname'])
     return render(request,'facultydetails.html',{'authors':queryset})  


def viewstupro(request):
    queryset=student.objects.all().filter(username=request.session['usrname'])
    return render(request,'studentdetails.html',{'authors':queryset})  
def viewallfac(request):
    queryset=faculty.objects.all().filter()
    return render(request,'allfaculty.html',{'authors':queryset})
def viewallstu(request):
    queryset=student.objects.all().filter()
    return render(request,'allstudent.html',{'authors':queryset})
def viewfacstud(request):
    queryset=student.objects.all().filter()
    return render(request,'fstuddetails.html',{'authors':queryset})
def viewfmarks(request):
    queryset=student.objects.all().filter()
    return render(request,'facmarks.html',{'authors':queryset})
def viewfacmarks(request):
     queryset=student.objects.all().filter()
     return render(request,'allstudmarks.html',{'authors':queryset})
def viewstudmarks(request):
     queryset=marks.objects.all().filter()
     return render(request,'allstudmarks.html',{'authors':queryset})


       



def fmarks(request):
    if request.method=='POST':
        studentid=request.POST.get('studentid')
        username=request.POST.get('username')
        assesmentno=request.POST.get('assesmentno')
        sub1=request.POST.get('sub1')
        sub2=request.POST.get('sub2')
        sub3=request.POST.get('sub3')
        percentage=request.POST.get('percentage')
        e=marks(studentid=studentid,username=username,assesmentno=assesmentno,sub1=sub1,sub2=sub2,sub3=sub3,percentage=percentage)
        e.save()
    return render(request,'facmarks.html')

def stuattendance(request):
    if request.method=='POST':
        date=request.POST.get('date')
        status_hour1=request.POST.get('status_hour1')
        status_hour2=request.POST.get('status_hour2')
        status_hour3=request.POST.get('status_hour3')
        status_hour4=request.POST.get('status_hour4')
        username=request.POST.get('username')
        studentid=request.POST.get('studentid')
       
        s=sattendance(date=date,status_hour1=status_hour1,status_hour2=status_hour2,status_hour3=status_hour3,status_hour4=status_hour4,username=username,studentid=studentid)
        s.save()
    return render(request,'facstudattendance.html')


def adminattendance(request):
     queryset=sattendance.objects.all().filter()
     return render(request,'studentattendance.html',{'authors':queryset})

def adminmarks(request):
    queryset=marks.objects.all().filter()
    return render(request,'admarks.html',{'authors':queryset})

def stumarks(request):
     queryset=marks.objects.all().filter(username=request.session['usrname'])
     return render(request,'studmarks.html',{'authors':queryset}) 
def stuattend(request):
     queryset=sattendance.objects.all().filter(username=request.session['usrname'])
     return render(request,'stuattendance.html',{'authors':queryset})       

def stuleave(request):
    if request.method=='POST':
        username=request.POST.get('username')
        batch=request.POST.get('batch')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
        sl=studentleave(username=username,batch=batch,fromdate=fromdate,todate=todate,reason=reason,status=status)
        sl.save()
    return render(request,'studentleave.html')

def facleave(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
        fl=facultyleave(username=username,fromdate=fromdate,todate=todate,reason=reason,status=status)
        fl.save()
    return render(request,'facultyleave.html')






def studleave(request):
     queryset=studentleave.objects.all().filter()
     return render(request,'adminleave.html',{'authors':queryset})
def approvestud(request):
    if request.method=='POST':
        username=request.POST.get('username')
        studentleave.objects.filter(username=username).update(status='Approved')
    return render(request,'adminleave.html')    

def approvedleave(request):
     queryset=studentleave.objects.all().filter(username=request.session['usrname'])
     return render(request,'studentleavestatus.html',{'authors':queryset})    

def approvefac(request):
     queryset=facultyleave.objects.all().filter()
     return render(request,'adminfacleave.html',{'authors':queryset})


def approvedfac(request):
    if request.method=='POST':
       username=request.POST.get('username')
       facultyleave.objects.filter(username=username).update(status='Approved')
    return render(request,'adminfacleave.html')    


def approvedstatusfac(request):
     queryset=facultyleave.objects.all().filter(username=request.session['usrname'])
     return render(request,'facultyleavestatus.html',{'authors':queryset})


def editdetails(request):
     queryset=faculty.objects.all().filter(username=request.session['usrname'])
     return render(request,'facultyedit.html',{'authors':queryset})  


def facdetailsedit(request):
    if request.method=='POST':
        facultyid=request.POST.get('facultyid')
        username=request.POST.get('username')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        batchincharge=request.POST.get('batchincharge')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        password=request.POST.get('password')
        faculty.objects.filter(username=request.session['usrname']).update(address=address,gender=gender,email=email,qualification=qualification,mobileno=mobileno, batchincharge=batchincharge,password=password)
    return redirect('facultyedit')
def editstud(request):
     queryset=student.objects.all().filter(username=request.session['usrname'])
     return render(request,'studentedit.html',{'authors':queryset})  
def studetailsedit(request):
    if request.method=='POST':
        studentid=request.POST.get('studentid')
        username=request.POST.get('username')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        admissiondate=request.POST.get('admissiondate')
        mobileno=request.POST.get('mobileno')
        password=request.POST.get('password')
        student.objects.filter(username=request.session['usrname']).update(address=address,gender=gender,email=email,mobileno=mobileno,password=password)
    return redirect('studentdetails')

def logout_view(request):
    logout(request)
    return redirect('login') 


def facstudentattendance(request):
     queryset=sattendance.objects.all().filter()
     return render(request,'facultystudattendance.html',{'authors':queryset})
