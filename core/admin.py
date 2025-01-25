from django.contrib import admin
from .models import  User, Student, TechTeam,Course, TeacherPage, Post, Video, File, Comment, Follow,Student,feedbacks,Enrollment
from django.contrib.auth.admin import UserAdmin


# Define the Admin classes with list_display and search_fields
class TeacherPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'module', 'followers', 'price']
    search_fields = ['name', 'title', 'module']  # Add any other fields you want to search by

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'salles', 'price']
    search_fields = ['name', 'category']  # Add any other fields you want to search by

class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'zoom_link', 'post_date', 'teacher']
    search_fields = ['text', 'zoom_link']  # Add any other fields you want to search by

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'likes', 'dislikes', 'views', 'duration', 'sequence_number']
    search_fields = ['name', 'course__name']  # Add any other fields you want to search by

class FileAdmin(admin.ModelAdmin):
    list_display = ['image', 'video']
    search_fields = ['image', 'video']  # Add any other fields you want to search by

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_postdate', 'text', 'video']
    search_fields = ['text', 'video__name']  # Add any other fields you want to search by

class FollowAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'student']
    search_fields = ['teacher__name', 'student__name']  # Add any other fields you want to search by

class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'feedback']
    search_fields = ['name', 'email', 'feedback']  # Add any other fields you want to search by

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'last_view', 'status']
    search_fields = ['course__name', 'student__name']  # Add any other fields you want to search by

# Register each model with its corresponding Admin class
admin.site.register(TeacherPage, TeacherPageAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(feedbacks, FeedbacksAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)



@admin.register(Student)
class StudentAdmin(UserAdmin):
    model = Student
    list_display = ('username', 'email', 'credit')
    fieldsets = (
        (None, {'fields': ('username', 'email','image', 'password','is_techteam','is_email_verified')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Credit', {'fields': ('credit',)}),  # Include the 'credit' field here
    )
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_techteam=False).order_by('username')
    

@admin.register(TechTeam)
class TechTeamAdmin(UserAdmin):
    
    model = TechTeam
    list_display = ('username', 'email','bio')
    def get_queryset(self,request):
        li=super().get_queryset(request)
        return li.filter(is_techteam=True).order_by('username')
