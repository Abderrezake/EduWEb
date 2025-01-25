from datetime import timedelta
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    credit = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,default=0)
    is_techteam = models.BooleanField(default=False)
    Password_last_Change = models.DateTimeField(default=timezone.now)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True,)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="tech_team_groups",
        related_query_name="tech_team_group",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="permissions",
        related_query_name="permission",
        help_text="Specific permissions for this user.",
    )
    class Meta(AbstractUser.Meta):
        permissions = [
            ('can_add_course', 'Can add courses'),
            ('can_delete_course', 'Can delete courses'),
            ('can_add_video', 'Can add videos'),
            ('can_delete_video', 'Can delete videos'),
            ('can_manage_credit', 'Can manage student credit'),]
        

class Student(User):
    
    class Meta:
        proxy = True
        verbose_name="student"
        verbose_name_plural="students"

    def __str__(self):
        return self.username + " (Student)"

class TechTeam(User):
    class Meta:
        proxy = True
        verbose_name="tech"
        verbose_name_plural="techs"

    def __str__(self):
        return self.username + " (Tech Team)"

class TeacherPage(models.Model):
    name = models.CharField(max_length=50)
    title=  models.CharField(max_length=50, default='استاذ')
    bio = models.CharField(max_length=200)
    experience = models.CharField(max_length=200,default='')
    Education = models.CharField(max_length=200,default='')
    email = models.EmailField()
    module=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    followers=models.DecimalField(max_digits=6, decimal_places=2)
    Emploit = models.ImageField(upload_to='images/',default='images/09.png')
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    

class Course(models.Model):
    name = models.CharField(max_length=50)
    category=models.CharField(max_length=50, default='others')
    section=models.CharField(max_length=50, default='others')
    level=models.DecimalField(max_digits=1,decimal_places=0,default=0)
    salles=models.DecimalField(max_digits=4, decimal_places=2,default=0)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)
    salles=models.DecimalField(max_digits=6, decimal_places=2,default=0)
    image = models.ImageField(upload_to='images/',default='core/img/science.png')
    bucket_link = models.CharField(max_length=255)
    service_account_key = models.FileField(upload_to='service_account_keys/',default='core/img/science.png')
    service_account_key_path = models.CharField(max_length=255,default="core/service_account_keys/") 

class Post(models.Model):
    text = models.CharField(max_length=50,null=True)
    zoom_link = models.URLField(max_length=100,default='',null=True)
    post_date = models.DateTimeField()
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)


class Video(models.Model):
    name = models.CharField(max_length=50)
    object_key = models.CharField(max_length=255)  # Assuming the object key can be up to 255 characters
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    likes=models.DecimalField(max_digits=4, decimal_places=2,default=0)
    dislikes=models.DecimalField(max_digits=4, decimal_places=2,default=0)
    views=models.DecimalField(max_digits=4, decimal_places=2,default=0)
    duration=models.DurationField(default=timedelta(seconds=0))
    sequence_number = models.IntegerField(default=0)  # Add this field



class File(models.Model):
    image = models.ImageField(upload_to='files/',default='core/img/science.png')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_postdate = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Follow(models.Model):
    
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,default=None)
    
class feedbacks(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name



class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    last_view = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices={('finiched','finiched'),('inProgress','inProgress'),('isntStart','isntStart')},default='isntStart')

    def __str__(self):
        return f"{self.student} - {self.course}"