from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    number = models.CharField(max_length=5)


class Student(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    number = models.CharField(max_length=8)

class Instructor(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    number = models.CharField(max_length=5)

class Lecture(models.Model):
    QR= models.IntegerField(primary_key=True) #QR ID for each Lecture of Each Course
    day= models.DateField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE)


class Enrollment(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)

class Attendance(models.Model):
    QR=models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
