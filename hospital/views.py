from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import department,doctor,appointment,register,login,slot
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.

def base(request):
    return render(request,'hospital/home.html')

def user(request):
    return render(request,'hospital/user.html')

def admin(request):
    return render(request,'hospital/admin.html')

def user_registration(request):
    if request.method=="POST":
        ob=register()
        ob.name=request.POST.get('name')
        ob.email=request.POST.get('email')
        ob.password=request.POST.get('password')
        ob.save()
        messages.success(request,"Account created successfully !")

        obj=login()
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('password')
        obj.u_id=ob.id
        obj.type="user"
        obj.save()
    return render(request,'hospital/user_registration.html')

def user_registered_list(request):
    ss=request.session['u_id']
    obj=register.objects.filter(id=ss)
    context={
        'x':obj
    }
    return render(request,'hospital/user_registered_list.html',context)

def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=login.objects.filter(email=email,password=password)
        tp=''
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=='user':
                request.session["u_id"]=uid
                return redirect('user')
            elif tp=='admin':
                request.session["u_id"]=uid
                return redirect('tempadmin')
        else:
                messages.warning(request,'Username/Password not found')
                return render(request,'hospital/login.html')
    return render(request,'hospital/login.html')

def admin_login(request):
    return render(request,'hospital/admin_login.html')

def department_list(request):
    ob=department.objects.all()
    context={
        'a':ob
    }
    return render(request,'hospital/department_list.html',context)

def update_department(request,id):
    ob=department.objects.get(pk=id)
    context={
        'x':ob
    }
    if request.method=="POST":
        obj=department.objects.get(pk=id)
        obj.name=request.POST.get('name')
        obj.save()
        return department_list(request)
    return render(request,'hospital/update_department.html',context)

def delete_department(request,id):
    ob=department.objects.get(pk=id)
    ob.delete()
    return department_list(request)

def create_doctor(request):
    abc=department.objects.all()
    context={
        'x':abc
    }
    if request.method=="POST":
        obj=doctor()
        obj.name=request.POST.get('name')
        obj.department_id=request.POST.get('department')
        # obj.image=request.POST.get('image')
        myfile = request.FILES['image']
        fd = FileSystemStorage()
        filename = fd.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.qualification=request.POST.get('qualification')
        obj.save()
        messages.success(request,"Account created successfully !")
    return render(request,'hospital/create_doctor.html',context)

def doctor_list(request):
    ab=doctor.objects.all()
    context={
        'y':ab
    }
    return render(request,"hospital/doctor_list.html",context)

def update_doctor(request,id):
    ob=doctor.objects.get(pk=id)
    if request.method=="POST":
        obj=doctor.objects.get(pk=id)
        obj.name=request.POST.get('name')
        obj.department_id=request.POST.get('department')
        myfile = request.FILES['image']
        fd = FileSystemStorage()
        filename = fd.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.qualification=request.POST.get('qualification')
        obj.save()
    return render("hospital/update_doctor.html",{'x':ob})

def appointment_form(request):
    ab=department.objects.all()
    cd=doctor.objects.all()
    context={
        'x':ab,
        'y':cd
    }
    if request.method=='POST':
        ur=request.session['u_id']
        ob=appointment()
        ob.name=request.POST.get('name')
        ob.email=request.POST.get('email')
        ob.phone=request.POST.get('phone')
        ob.place=request.POST.get('place')
        ob.date=request.POST.get('date')
        ob.time=request.POST.get('time')
        ob.department_id=request.POST.get('department')
        ob.doctor_id=request.POST.get('doctor')
        ob.status='pending'
        ob.appointment_id=ur
        ob.save()
        messages.success(request,'Appointment booking is successfull !')
    return render(request,'hospital/appointment_form.html',context)

def appointment_form_list(request):
    ur=request.session['u_id']
    obj=register.objects.filter(id=ur)
    context={
        'x':obj
    }
    return render(request,'hospital/appointment_list.html',context)

def manage_appointment(request):
    ob = appointment.objects.all()
    context = {
        's': ob
    }
    return render(request,'hospital/manage_appointment.html',context)

def appointment_approve(request,id):
    ob=appointment.objects.get(appointment_id=id)
    ob.status='APPROVED'
    ob.save()
    return manage_appointment(request)

def appointment_reject(request,id):
    ob = appointment.objects.get(appointment_id=id)
    ob.status = 'REJECTED'
    ob.save()
    return manage_appointment(request)

def add_slot(request):
    return render(request,'hospital/add_slot.html')

