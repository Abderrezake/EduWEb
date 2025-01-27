from decimal import Decimal
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Follow,TeacherPage,feedbacks,Course,Video,Enrollment,Course,Student, TechTeam,Post,ChatThread, ChatMessage
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
from google.cloud import storage
from google.oauth2 import service_account
import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils import timezone
def main_page(request):
    teachers = TeacherPage.objects.all().order_by('-followers')[:3]
    courses = Course.objects.all().order_by('-salles')[:3]
    context={
        'teachers': teachers,
        'courses': courses
    }
    return render(request, 'core/main.html', context)

def log_view(request):
    return render(request, 'core/log.html')
    
    
    #Teachers Page 

@login_required(login_url='/log')
def teachers_list(request):
    teachers = TeacherPage.objects.all()
    # Handle search query
    query = request.GET.get('q')
    if query:
        teachers = teachers.filter(name__icontains=query)

    return render(request,'core/teachers.html', {'teachers': teachers})

@login_required(login_url='/log')
def teacher_page(request,teacher_name):
    student = request.user
    teacher = get_object_or_404(TeacherPage, name=teacher_name)
    posts = Post.objects.filter(teacher=teacher)
    courses = Course.objects.filter(teacher=teacher)
    follow = Follow.objects.filter(teacher=teacher,student=student).exists()
    tech_member=(student.is_techteam==True)
    
    context = {
        'teacher': teacher,
        'posts': posts,
        'courses': courses,
        'follow': follow,
        'is_tech': tech_member
    }
    return render(request, 'core/Teacher_page.html', context)

@login_required(login_url='/log')
def follow_teacher(request,teacher_name):
    # Get the current student
    student = request.user

    try:
        # Get the teacher object based on the teacher_name
        teacher_page = TeacherPage.objects.get(name=teacher_name)

        # Check if the student has enough credit to buy the course
        if student.credit and Decimal(student.credit) >= teacher_page.price:
            # Reduce the student's credit by the course price
            student.credit -= teacher_page.price
            student.save()

            # Add the course to the enrollment table
            Follow.objects.create(teacher=teacher_page, student=student)

            # Redirect to the main page or any other page
            return redirect(reverse('core:teacher', args=[teacher_name]))
        else:
            # If the student does not have enough credit, show an error message
            return HttpResponse("You do not have enough credit to buy this course.")
    except Course.DoesNotExist:
        # If the course does not exist, show an error message
        return HttpResponse("Course not found.")
    
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password,model=User)
        if user is not None :
            if user.is_email_verified:
                login(request, user)
                return redirect('core:main')
            else :
                    return render(request, 'core/log.html', {'error_message1': 'your email are not verified'})
        else:
            return render(request, 'core/log.html', {'error_message1': 'Invalid login'})
    # If GET or any other method, render the log form
    return redirect('core:log')

def signup_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request,'core/log.html',{'error_message2':'username or email not available'})
        user = get_user_model().objects.create_user(email=email, password=password,username=username, is_email_verified=False)
        token = default_token_generator.make_token(user)
        verification_url = reverse('core:verify_email', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': token})
        verification_link = f'http://{get_current_site(request)}{verification_url}'
        message = render_to_string('core/verification_email.html', {'user': user, 'action_url': verification_link})
        send_mail('Veuillez vérifier votre adresse email',message, 'schoolinenotif@gmail.com', [user.email],html_message=message)
        return render(request,'core/log.html',{'error_message2':'Veuillez vérifier votre adresse email'})
    return redirect('core:log')

def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.save()
        user = authenticate(username=user.username, password=user.password,model=User)
        return redirect('core:main')
    else:
        return render(request,'core/log.html',{'error_message2':'email cant be verified'})
    


# feedback 

@login_required(login_url='/log')
def dashboard(request):
    user = request.user

    # Initialize context variables
    nbr_courses = None
    teachers = None
    courses = None
    chat_threads = None
    all_messages = None
    chat_threads_data = []

    if user.is_techteam:  # Admin/TechTeam view
        chat_threads = ChatThread.objects.prefetch_related('messages').all()
        all_messages = ChatMessage.objects.select_related('thread', 'sender').order_by('timestamp')

        # Prepare chat threads with the last message
        for thread in chat_threads:
            last_message = all_messages.filter(thread=thread).last()
            chat_threads_data.append({
                'thread': thread,
                'last_message': last_message,
            })
    else:  # Student view
        nbr_courses = Enrollment.objects.filter(student=user).count()
        teachers = Follow.objects.filter(student=user).distinct()
        courses = Enrollment.objects.filter(student=user).order_by('-last_view')
        chat_thread = get_object_or_404(ChatThread, student=user)
        all_messages = ChatMessage.objects.filter(thread=chat_thread).order_by('timestamp')

    # Construct context
    context = {
        'user': user,
        'nbr_courses': nbr_courses,
        'teachers': teachers,
        'courses': courses,
        'chat_threads': chat_threads_data if user.is_techteam else chat_thread,
        'all_messages': all_messages ,
    }

    return render(request, 'core/Dashboard.html', context)

@login_required(login_url='/log')
def submit_feedback(request):
    if request.method == 'POST':
        person = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Check if all required fields are provided
        if not person or not email or not message:
            return HttpResponseBadRequest('Please fill in all fields.')

        # Save feedback
        feedback = feedbacks.objects.create(name=person, email=email, feedback=message)
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('core:main')
    
    else:
        teachers = TeacherPage.objects.all().order_by('-followers')[:3]
        return render(request, 'core/teachers.html', {'teachers': teachers})
#courses
@login_required(login_url='/log')
def courses_list(request, category,level):
    courses = Course.objects.all().order_by('-salles')
    # Handle search query
    query = request.GET.get('q')
    if query:
        courses = courses.filter(name__icontains=query)
    courses =courses.filter(level=level)
    context = {'courses': courses, 'category': category,'level':level}
    return render(request, 'core/courses.html', context)

login_required(login_url='/log')
def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('core:main')

@login_required(login_url='/log')
def buying_course(request, course_name):
    # Get the current student
    student = request.user

    try:
        # Get the course object based on the course name
        course = Course.objects.get(name=course_name)

        # Check if the student is already enrolled in the course
        enrollment_exists = Enrollment.objects.filter(course=course, student=student).exists()

        if enrollment_exists:
            # If the student is already enrolled, show a message or redirect
            return HttpResponse("You are already enrolled in this course.")
        
        # Check if the student has enough credit to buy the course
        if student.credit and Decimal(student.credit) >= course.price:
            # Reduce the student's credit by the course price
            student.credit -= course.price
            student.save()

            # Add the course to the enrollment table
            Enrollment.objects.create(course=course, student=student)

            # Redirect to the main page or any other page
            return redirect('core:main')
        else:
            # If the student does not have enough credit, show an error message
            return HttpResponse("You do not have enough credit to buy this course.")
    except Course.DoesNotExist:
        # If the course does not exist, show an error message
        return HttpResponse("Course not found.")
    


@login_required(login_url='/log')
def video_page(request, course_name, video_id):
    
    # Get the current student
    student = request.user

    try:
        # Get the course object based on the course name
        course = Course.objects.get(name=course_name)

        # Check if the student is enrolled in the course
        enrollment = Enrollment.objects.get(course=course, student=student)
    except Enrollment.DoesNotExist:
        # If the student is not enrolled, redirect them to a different page or show an error message
        return redirect(reverse('core:buy', args=[course_name]))

    # Path to your service account key file
    key_path = 'path_to_your_service_account_key.json'

    # Authenticate using the service account key file
    credentials = service_account.Credentials.from_service_account_file(key_path)
    client = storage.Client(credentials=credentials)

    # Name of your GCS bucket
    bucket_name = 'your_bucket_name'

    # Get the course object based on the course name
    course = Course.objects.get(name=course_name)

    # Get a list of videos for the specific course
    videos = Video.objects.filter(course=course)

    # Get the total duration of all videos
    total_duration = sum(video.duration for video in videos)

    # Get the total number of videos
    total_videos = len(videos)

    # Get the video object for the specified video_id from the list of videos
    video = videos.filter(id=video_id).first()
    
    # Name of the video file in your bucket based on the video_id
    blob_name = video.object_key

    # Get a reference to the video file
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Generate a signed URL that expires in 1 hour
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    signed_url = blob.generate_signed_url(expiration=expiration, method='GET')

    # Pass the videos list, signed URL, and other context data to the template
    context = {
        'videos': videos,
        'signed_url': signed_url,
        'course': course,
        'video_id': video_id,
        'total_duration': total_duration,
        'total_videos': total_videos,
    }
    return render(request, 'video.html', context)

@login_required(login_url='/log')
def change_password(request):
    if request.method == 'POST':
        user= request.user
        new_password = request.POST.get('password')
        user.Password_last_Change =timezone.now()
        user.set_password(new_password)
        user.save()
        logout(request) 

    return render(request,'core/log.html',{'error_message1':'enter the new password'})

@login_required(login_url='/log')
def change_name(request):

    if request.method == 'POST':
        user= request.user
        new_name = request.POST.get('username')
        user.username=new_name
        user.save()

    return redirect('core:dashboard')

@login_required(login_url='/log')
def change_email(request):
    if request.method == 'POST':
        user= request.user
        new_email = request.POST.get('email')
        user.email = new_email
        user.is_is_email_verified =False
        user.save()
        logout(request)  
        token = default_token_generator.make_token(user)
        verification_url = reverse('core:verify_email', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': token})
        verification_link = f'http://{get_current_site(request)}{verification_url}'
        message = render_to_string('core/verification_email.html', {'user': user, 'action_url': verification_link})
        send_mail('Veuillez vérifier votre adresse email',message, 'schoolinenotif@gmail.com', [user.email],html_message=message)
        return render(request,'core/log.html',{'error_message1':'Veuillez vérifier votre adresse email'})
@login_required(login_url='/log')
def add_post(request,id):
    #user= request.user
    post=Post.objects.create(text=request.POST.get('text'),post_date=timezone.now(),teacher=TeacherPage.objects.get(id=id),zoom_link=request.POST.get('url'))
    post.save()
    for u in Follow.objects.filter(teacher=TeacherPage.objects.get(id=id)):
        user=User.objects.get(id=u.student.id)
        message = render_to_string('core/not.html', {'user': user.username,'post':post})
        send_mail('notification de zoom',message, 'schoolinenotif@gmail.com', [user.email],html_message=message)
    return redirect('core:main')


@login_required(login_url='/log')
def add_message(request):
    if request.method == 'POST':
        # Get the form data
        message_content = request.POST.get('message')
        sender = request.user

        # Validate the message content
        if not message_content:
            return redirect('core:dashboard')  # Redirect even if the message is empty (or handle as needed)

        # Determine the thread
        if sender.is_techteam:  # Tech team member
            thread_id = request.POST.get('thread_id')
            if not thread_id:
                return redirect('core:dashboard')  # Redirect if thread ID is missing
            thread = get_object_or_404(ChatThread, id=thread_id)
        else:  # Student
            thread = get_object_or_404(ChatThread, student=sender)

        # Create and save the message
        ChatMessage.objects.create(
            thread=thread,
            sender=sender,
            content=message_content,
        )

        # Redirect to the dashboard after successful submission
        return redirect('core:dashboard')

    # Handle non-POST requests by redirecting to the dashboard
    return redirect('core:dashboard')