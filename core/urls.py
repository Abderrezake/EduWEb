from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.main_page, name='main'),
    path('log/', views.log_view, name='log'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
    path('Teachers/', views.teachers_list, name='Teachers'),
    re_path(r'^videos/(?P<course_name>[\w\s\d\-_.\u0600-\u06FF]+)/(?P<video_id>\d+)$', views.video_page, name='videos'),
    re_path(r'^Buy/(?P<course_name>[\w\s\d\-_.\u0600-\u06FF]+)/$', views.buying_course, name='buy'),
    re_path(r'^courses/(?P<category>[\w\s\d\-_.\u0600-\u06FF]+)/(?P<level>[\w\s\d\-_.\u0600-\u06FF]+)/$', views.courses_list, name='courses'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_name/', views.change_name, name='change_name'),
    path('change_email/', views.change_email, name='change_email'),
    re_path(r'^teacher/(?P<teacher_name>[\w\s\d\-_.\u0600-\u06FF]+)/$', views.teacher_page, name='teacher'),
    re_path(r'^Follow/(?P<teacher_name>[\w\s\d\-_.\u0600-\u06FF]+)/$', views.follow_teacher, name='Follow_page'),
    path('add_post/<int:id>', views.add_post, name='add_post'),

    # other URL patterns
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
