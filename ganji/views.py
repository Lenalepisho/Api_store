from django.shortcuts import render, redirect
from .models import Enroll
from .forms import EnrollForm

# Create your views here.
def home(request):
    """DISPLAIYING HOME.HTML"""
    return render(request, 'index.html')
def about(request):
    """DISPLAYING ABOUT.HTML"""
    return render(request, 'about.html')
# note: detailed enroll view is defined further below and handles POST submissions
def contact(request):
    """DISPLAYING CONTACT.HTML"""
    return render(request, 'contact.html')
def courses(request):
    """DISPLAYING COURSES.HTML"""
    return render(request, 'courses.html')

def instructors(request):
    """DISPLAYING INSTRUCTORS.HTML"""
    return render(request, 'instructors.html')

def pricing(request):
    """DISPLAYING PRICING.HTML"""
    return render(request, 'pricing.html')

def blog(request):
    """DISPLAYING BLOG.HTML"""
    return render(request, 'blog.html')

def course_detail(request, course_id):
    """DISPLAYING COURSE_DETAIL.HTML"""
    return render(request, 'course_detail.html', {'course_id': course_id})

#function to push data to database
def enroll(request):
    """HANDLE ENROLLMENT FORM SUBMISSION"""
    selected_course = request.GET.get('course', '') if request.method == 'GET' else request.POST.get('select_course', '')
    success = False
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = EnrollForm(initial={'select_course': selected_course})
    else:
        form = EnrollForm(initial={'select_course': selected_course})

    return render(request, 'enroll.html', {
        'form': form,
        'success': success,
        'selected_course': selected_course,
    })

#retrieve all enrollments 
def read_enroll(request):
    """create a view to read and display all enrollments"""
    enrollments = Enroll.objects.all()  # Get all enrollment records
    context={'enrollments': enrollments}  # Pass the enrollments to the template context
    return render(request, 'show_enrollment.html', context)

#delete enrollment
def delete_enroll(request, enroll_id):
    """create a view to delete an enrollment"""
    enrollment = Enroll.objects.get(id=enroll_id)  # Get the enrollment record by ID
    enrollment.delete()  # Delete the record from the database
    return redirect('ganji:show_enrollment')  # Redirect back to the enrollment list view

#update enrollment
def update_enroll(request, enroll_id):
    """create a view to update an enrollment"""
    enrollment = Enroll.objects.get(id=enroll_id)  # Get the enrollment record by ID
    if request.method == 'POST':
        # Update the enrollment fields with new data from the form
        enrollment.name = request.POST.get('name', enrollment.name)
        enrollment.email = request.POST.get('email', enrollment.email)
        enrollment.select_course = request.POST.get('course', enrollment.select_course)
        enrollment.phone_number = request.POST.get('phone', enrollment.phone_number)
        enrollment.what_motivates_you_to_take_this_course = request.POST.get('motivation', enrollment.what_motivates_you_to_take_this_course)
        enrollment.experience_level = request.POST.get('experience', enrollment.experience_level)
        enrollment.education_level = request.POST.get('education', enrollment.education_level)
        enrollment.preferred_learning_schedule = request.POST.get('schedule', enrollment.preferred_learning_schedule)
        enrollment.i_agree = request.POST.get('terms') == 'on'
        enrollment.i_would_like_to_receive_updates = request.POST.get('newsletter') == 'on'
        enrollment.save()
        return redirect('ganji:show_enrollment')
    
    context = {'enrollment': enrollment}
    return render(request, 'update_enrollment.html', context)

