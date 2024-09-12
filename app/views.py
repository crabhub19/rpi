from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import *
import os
# Create your views here.

def index(request):
    department = Department.objects.all()
    contex = {
        'department':department
    }
    return render(request,'index.html',contex)

# student++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
def student(request,dept):
    contex={
    'student': Student.objects.all(),
    'dept':dept
    }
    request.session['student']=request.build_absolute_uri()
    return render(request,'student.html',contex)
# instructor+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def instructor(request,dept):
    contex={
    'instructor': Instructor.objects.all(),
    'dept':dept
    }
    request.session['instructor']=request.build_absolute_uri()
    return render(request,'instructor.html',contex)
#instrument_________________________________________________________________
def instrument(request,dept):
    contex={
        'instrument': Instrument.objects.all(),
        'dept':dept
    }
    request.session['instrument']=request.build_absolute_uri()
    return render(request,'instrument.html',contex)

# notice_________________________________________________________
def notice(request):
    contex={
    'notice': Notice.objects.all().order_by("-created_at")
    }
    return render(request,'notice.html',contex)

# login_requre+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# add all thing______________________________________________________---------------

#add_student________________________________________________________________-
@login_required(login_url='user_login')
def add_student(request):
    contex = {
        'department' : Department.objects.all()
    }
    if request.method=="POST":
        name=request.POST.get("name")
        roll=request.POST.get("roll")
        email=request.POST.get("email")
        went=request.POST.get("went")
        address=request.POST.get("address")
        description=request.POST.get("description")
        gender=request.POST.get("gender")
        department_id=request.POST.get("department")
        department = Department.objects.get(pk=department_id)
        cr=request.POST.get("cr")
        firstShift=request.POST.get("firstShift")
        secondShift=request.POST.get("secondShift")
        studentImage=request.FILES.get("studentImage")
        exists_name = Student.objects.filter(name=name).exists()
        exists_email = Student.objects.filter(email=email).exists()
        exists_roll = Student.objects.filter(roll=roll).exists()
        if exists_name :
            messages.error(request,"name have already takken")
            return redirect('add_student')
        if exists_roll :
            messages.error(request,"roll have already takken")
            return redirect('add_student')
        if exists_email :
            messages.error(request,"email have already takken")
            return redirect('add_student')


        student= Student(name=name,roll=roll,email=email,went=went,address=address,description=description,gender=gender,department=department,cr=cr,firstShift=firstShift,secondShift=secondShift,studentImage=studentImage)
        messages.success(request,"you have successed to store data")
        student.save()
        return redirect('add_student')
    return render(request,'add_student.html',contex)


    #add_insructor______________________________________________________________________
@login_required(login_url='user_login')
def add_instructor(request):
    contex = {
        'department' : Department.objects.all()
    }
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        tag=request.POST.get("tag")
        address=request.POST.get("address")
        description=request.POST.get("description")
        gender=request.POST.get("gender")
        department_id=request.POST.get("department")
        department = Department.objects.get(pk=department_id)
        rank=request.POST.get("rank")
        firstShift=request.POST.get("firstShift")
        secondShift=request.POST.get("secondShift")
        instructorImage=request.FILES.get("instructorImage")
        exists_name = Instructor.objects.filter(name=name).exists()
        exists_email = Instructor.objects.filter(email=email).exists()
        if exists_name :
            messages.error(request,"name have already exist")
            return redirect('add_instructor')
        if exists_email :
            messages.error(request,"email have already exist")
            return redirect('add_instructor')


        instructor= Instructor(name=name,email=email,tag=tag,address=address,description=description,gender=gender,department=department,rank=rank,firstShift=firstShift,secondShift=secondShift,instructorImage=instructorImage)
        messages.success(request,"you have successed to store data")
        instructor.save()
        return redirect('add_instructor')
    return render(request,'add_instructor.html',contex)



    #_add_instrument_________________________________________________________________________________
@login_required(login_url='user_login')
def add_instrument(request):
    contex = {
        'department' : Department.objects.all()
    }
    if request.method=="POST":
        name=request.POST.get("name")
        closet=request.POST.get("closet")
        rack=request.POST.get("rack")
        department_id=request.POST.get("department")
        department = Department.objects.get(pk=department_id)
        instrumentImage=request.FILES.get("instrumentImage")
        exists_name = Instructor.objects.filter(name=name).exists()
        if exists_name :
            messages.error(request,"instrument have already exist")
            return redirect('add_instrument')
        instrument = Instrument(name=name,closet=closet,rack=rack,department=department,instrumentImage=instrumentImage)
        instrument.save()
        messages.success(request,"your instrument have been added")
        return redirect('add_instrument')
    return render(request,'add_instrument.html',contex)

# add_department++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
@login_required(login_url='user_login')
def add_department(request):
    if request.method=="POST":
        name=request.POST.get("name")
        desc=request.POST.get("description")
        exists_name = Department.objects.filter(name=name).exists()
        if exists_name :
            messages.error(request,"department have already exist")
            return redirect('add_department')
        department = Department(name=name,bio=desc)
        department.save()
        messages.success(request,"your department have been added")
        return redirect('add_department')
    return render(request,'add_department.html')

# add_notice_____________________________________________
def add_notice(request):
    if request.method=="POST":
        heading=request.POST.get("heading")
        details=request.POST.get("details")
        noticeImage=request.FILES.get("noticeImage")
        notice = Notice(heading=heading,details=details,noticeImage=noticeImage)
        notice.save()
        messages.success(request,"your notice have been published")
        return redirect('notice')
    return render(request,'add_notice.html')

    #signup-------------------------------------------------------------------------------
def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirmPassword=request.POST.get("confirmPassword")
        exists_user = User.objects.filter(username=username).exists()
        if exists_user:
            messages.error(request,"user have already exist")
            return redirect('signup')
        if password == confirmPassword:
            my_user = User.objects.create_user(username=username,password=password)
            my_user.save()
            login(request, my_user)
            messages.success(request,'user have been created')
            return redirect('/')
        else:
            messages.error(request,"password not same")
            return redirect('signup')
    return render(request,'signup.html')



# delete all thing______________________________-------------------------------

# delete_instrument++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='user_login')
def delete_instrument(request,pk):
    instrument = Instrument.objects.get(id=pk)
    if len(instrument.instrumentImage)>0:
        image_path = instrument.instrumentImage.path
        if os.path.exists(image_path):
            os.remove(image_path)
        instrument.instrumentImage.delete()
    instrument.delete()
    messages.success(request,"delete successfully")
    previous_url = request.session.get('instrument')
    return redirect(previous_url)



# delete_instructor++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='user_login')
def delete_instructor(request,pk):
    instructor = Instructor.objects.get(id=pk)
    if len(instructor.instructorImage)>0:
        image_path = instructor.instructorImage.path
        if os.path.exists(image_path):
            os.remove(image_path)
        instructor.instructorImage.delete()
    instructor.delete()
    messages.success(request,"delete successfully")
    previous_url = request.session.get('instructor')
    return redirect(previous_url)


# delete_student++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='user_login')
def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    if len(student.studentImage)>0:
        image_path = student.studentImage.path
        if os.path.exists(image_path):
            os.remove(image_path)
        student.studentImage.delete()
    student.delete()
    messages.success(request,"delete successfully")
    previous_url = request.session.get('student')
    return redirect(previous_url)

# delete_department++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='user_login')
def delete_department(request,pk):
    department = Department.objects.get(id=pk)
    department.delete()
    messages.success(request,"delete successfully")
    return redirect('/')


# delete_notice  +++++++++++++++++++++++-----------------------------------
@login_required(login_url='user_login')
def delete_notice(request,pk):
    notice = Notice.objects.get(id=pk)
    if len(notice.noticeImage)>0:
        image_path = notice.noticeImage.path
        if os.path.exists(image_path):
            os.remove(image_path)
        notice.noticeImage.delete()
    notice.delete()
    messages.success(request,"delete successfully")
    return redirect('notice')



#login-------------------------------------------------------------
def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if user.is_active:
            #     request.session.set_expiry(86400)
            #     request.session['user_id'] = user.id
            messages.success(request,"confirm that you are one of us")
            return redirect('/')
        else:
            messages.error(request,"username or password was worng")
            return redirect('user_login')
    return render(request,'user_login.html')


# logout_________________________________________________________________________
def user_logout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('/')


# search_____________________________________________________
def search(request):
    query = request.GET.get('q')
    if query:
        student = Student.objects.filter(Q(name__icontains=query) | Q(roll__icontains=query) | Q(email__icontains=query))
        instructor = Instructor.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
        instrument = Instrument.objects.filter(Q(name__icontains=query))
    else:
        student = Student.objects.all()
        instructor = Instructor.objects.all()
        instrument = Instrument.objects.all()
    # return render(request,'search.html')
    return render(request,'search.html',{'query':query,'student':student,'instructor':instructor,'instrument':instrument,})

