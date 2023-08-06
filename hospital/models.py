from django.db import models

# Create your models here.
class department(models.Model):
    department_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class doctor(models.Model):
    doctor_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    qualification=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class appointment(models.Model):
    appointment_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    place=models.CharField(max_length=150)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    doctor=models.ForeignKey(doctor,models.CASCADE)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    u_id=models.IntegerField()

    def __str__(self):
        return self.email
    
class slot(models.Model):
    slot_id=models.AutoField(primary_key=True)
    time_slot=models.CharField(max_length=100)