from django.shortcuts import render,redirect, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth.hashers import check_password
import json
from django.contrib.auth.decorators import login_required

# 

def home(request):
    return render(request,'index.html',{'home_bg':True,'show_bg':True})

def success(request):
        return render(request,'success.html',{'form_bg':True})


def dashboard(request):
    user_type = request.session.get('user_type')

    # Fetch total counts
    total_staff = Staff.objects.all().count()
    total_students = Student.objects.all().count()
    total_assignments = Assignment.objects.all().count()

    # Fetch assignments (recent for display)
    recent_assignments = Assignment.objects.order_by('-created_at')[:3]

    # Prepare data for the chart
    chart_data = json.dumps([total_students, total_staff, total_assignments])

    context = {
        'user_type': user_type,
        'total_staff': total_staff,
        'total_students': total_students,
        'total_assignments': total_assignments,
        'recent_assignments': recent_assignments,
        'chart_data': chart_data,  # Pass the serialized data here
    }
    return render(request, 'dashboard.html', context)


def student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student profile saved successfully!")
            return redirect('student_list')
        else:
            print("Form errors:", form.errors)  # Debugging line
            messages.error(request, "Error submitting the form!")
    else:
        form = StudentProfileForm()

    return render(request, 'student_profile.html', {'form': form})


def staff_profile(request):
    if request.method == 'POST':
        form = StaffProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff profile saved successfully!")
            return redirect('staff_list')
        else:
            print("Form errors:", form.errors)  # Debugging line
            messages.error(request, "Error submitting the form!")
    else:
        form = StaffProfileForm()

    return render(request, 'staff_profile.html', {'form': form})


def student_info(request,id):
    try:
        stud = Student.objects.get(id=id)

    except Student.DoesNotExist:
        messages.error(request,'Student not found')
        return redirect('student_profile')
    
    return render(request,'student_info.html',{'stud':stud})

def staff_info(request,id):
    try:
        staff = Staff.objects.get(id=id)

    except Staff.DoesNotExist:
        messages.error(request,'Staff not found')
        return redirect('staff_profile')
    
    return render(request,'staff_info.html',{'staff':staff})


def staff_update(request,id):
    try:
        staff = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        messages.error(request,'staff not found ')
    if request.method == 'POST':
        form=StaffProfileForm(request.POST,request.FILES,instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request,'Staff Update Successfull')
            return redirect('staff_info',id=staff.id)
        else:
            messages.error(request,'Error Updating Staff')

    form = StaffProfileForm(instance=staff)
    return render(request,'staff_update.html',{'staff':staff,'form':form})

def student_update(request,id):
    try:
        stud = Student.objects.get(id=id)
    except Staff.DoesNotExist:
        messages.error(request,'Student not found ')
    if request.method == 'POST':
        form=StudentProfileForm(request.POST,request.FILES,instance=stud)
        if form.is_valid():
            form.save()
            messages.success(request,'Student Update Successfull')
            return redirect('student_info',id=stud.id)
        else:
            messages.error(request,'Error Updating Student')

    form = StudentProfileForm(instance=stud)
    return render(request,'student_update.html',{'stud':stud,'form':form})

def student_list(request):
    stud = Student.objects.all()
    context = {'stud':stud}
    return render(request,'student_list.html',context)

def staff_list(request):
    staff = Staff.objects.all()
    context = {'staff':staff}
    return render(request,'staff_list.html',context)


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['c_password']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user_type = form.cleaned_data['user_type']

            # Check if passwords match
            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
            elif Sign_Up.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            elif Sign_Up.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
            else:
                # Create a new User object
                user = User(username=username, email=email)
                user.set_password(password)  # Hash the password
                user.save()  # Save the User instance

                # Save additional data in Sign_Up model
                Sign_Up.objects.create(
                    user=user,
                    user_type=user_type,
                    username=username,
                    email=email,
                    password=user.password  # Save the hashed password
                )

                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('sign_in')
    else:
        form = SignUpForm()
    
    return render(request, 'sign_up.html', {'form': form})



def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            try:
                # Fetch user based on username and user_type
                profile = Sign_Up.objects.get(username=username, user_type=user_type)

                # Verify password
                if check_password(password, profile.password):
                    # Set session data
                    request.session['username'] = profile.username
                    request.session['user_type'] = profile.user_type
                    messages.success(request, "Login successful!")
                    return redirect('home')  # Adjust 'dashboard' to your URL name
                else:
                    messages.error(request, "Invalid password!")
            except Sign_Up.DoesNotExist:
                messages.error(request, "Invalid username or user type!")
    else:
        form = SignInForm()
    
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request,'Successfully logged out..!')
    return redirect('home')



def create_assignment(request):
        if request.method == 'POST':

            form = AssignmentForm(request.POST)
            if form.is_valid():
                assignments = form.save(commit=False)
                assignments.save()
                form.save_m2m()  # Save the many-to-many field data
                return redirect('assignment_list')  # Redirect to the assignment list page
        else:
            form = AssignmentForm()
        return render(request, 'create_assignment.html', {'form': form})



#assignments view................................
def student_assignments(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'student_assignments.html', context)  

#list of assignments.................................
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request,'assignment_list.html',{'assignments': assignments})