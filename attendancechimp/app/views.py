#django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied

#from my model
import datetime as dt
import calendar
from .models import *
from django.utils import timezone
from datetime import datetime
from django.utils import timezone


@csrf_exempt
def index(request):
    if request.method == "GET":
        datetime = timezone.localtime(timezone.now())
        return render(request, 'app/index.html', {'datetime': datetime})
   
    raise PermissionDenied

@csrf_exempt
def new(request):
    """
    The page for creating a new user

    Error checking:
    - this view only triggers on a GET request.
    - this view only triggers if the user isn't logged in
    """

    # only go to this page if not logged in
    if request.method == "GET" and not request.user.is_authenticated:
        return render(request, 'app/new.html', {})
   
    raise PermissionDenied
   
@csrf_exempt
def course_create(request):
    """The page for creating a new course

    Error checking:
    - this view only triggers on a GET request.
    - this view fails if the user isn't logged in
    - view fails if the linkage between UniversityPerson and User breaks
    """

    # don't allow not logged in users to do this
    if not request.user.is_authenticated or request.method == "POST":
        raise PermissionDenied

    # get the logged in user
    up = UniversityPerson.objects.filter(user_id=request.user.id)

    # fatal error
    if len(up) == 0:
        raise PermissionDenied

    up = up[0]

    return render(request, 'app/course_create.html', {'is_student': not up.is_instructor})

@csrf_exempt
def qr_create(request):
    """The page for creating a QR code

    Error checking:
    - this view only triggers on a GET request.
    - this view fails if the user isn't logged in
    - view fails if the linkage between UniversityPerson and User breaks
    """

    if not request.user.is_authenticated or request.method == "POST":
        raise PermissionDenied

    # get the logged in user
    up = UniversityPerson.objects.filter(user_id=request.user.id)

    # fatal error
    if len(up) == 0:
        raise PermissionDenied

    up = up[0]
    courses = Course.objects.filter(instructor=up)

    return render(request, 'app/qr_create.html', {'courses': courses, 'is_student': not up.is_instructor})

@csrf_exempt
def qr_upload(request, errors=""):
    """The page for uploading a QR code

    Error checking:
    - this view fails if the user isn't logged in
    - view fails if the linkage between UniversityPerson and User breaks
    """

    if not request.user.is_authenticated:
        raise PermissionDenied

    # get the logged in user
    up = UniversityPerson.objects.filter(user_id=request.user.id)

    # fatal error
    if len(up) == 0:
        raise PermissionDenied

    up = up[0]

    return render(request, 'app/qr_upload.html', {'is_student': not up.is_instructor, 'errors': errors})

@csrf_exempt
def new_submit(request):
    """Handles a submission from a new user creation form.

    Error Checking:
    - Raises an error if logged in
    """

    # is a user logged in, if so fail
    if request.user.is_authenticated:
        raise PermissionDenied

    # get the post data
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    is_instructor = (request.POST.get("choice") == "instructor")

    # return back if there is some kind of an error
    if username is None or\
       email is None or\
       password is None or\
       request.POST.get("choice") is None:
           return render(request, 'app/new.html', {})
   
    # create and login
    user, _ = create_ac_user(username, email, password, is_instructor)
    login(request, user)
   
    #create and login
    return render(request, 'app/index.html',{})

@csrf_exempt
def handle_form(request):

    cname = request.POST['cname']
    cnum =  request.POST['cnum']

    print(cname, cnum)

    new_course = Course(cname, cnum)
    new_course.save()

    return render(request, 'app/index.html', {})
