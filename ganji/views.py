from django.shortcuts import render, redirect
from .models import Enroll

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
    if request.method == 'POST':
        # Extract form data (match template field names)
        first_name = request.POST.get('firstName', '').strip()
        last_name = request.POST.get('lastName', '').strip()
        name = f"{first_name} {last_name}".strip()
        email = request.POST.get('email')
        course = request.POST.get('course')
        number = request.POST.get('phone')
        message = request.POST.get('motivation')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        preferred_learning_schedule = request.POST.get('schedule')
        i_agree = request.POST.get('terms') == 'on'  # Convert to boolean
        i_would_like_to_receive_updates = request.POST.get('newsletter') == 'on'  # Convert to boolean
        
        # Create a new enrollment object and save it to the database
        enrollment_obj = Enroll(
            name=name,
            email=email,
            select_course=course,
            phone_number=number,
            what_motivates_you_to_take_this_course=message,
            experience_level=experience,
            education_level=education,
            preferred_learning_schedule=preferred_learning_schedule,
            i_agree=i_agree,
            i_would_like_to_receive_updates=i_would_like_to_receive_updates
        )
        enrollment_obj.save()
        return redirect('ganji:index')
        
    return render(request, 'enroll.html')

#retrieve all enrollments 
def read_enroll(request):
    """create a view to read and display all enrollments"""
    enrollments = Enroll.objects.all()  # Get all enrollment records
    context={'enrollments': enrollments}  # Pass the enrollments to the template context
    return render(request, 'show_enrollment.html', context)

#delte enrollment
def delete_enroll(request, enroll_id):
    """create a view to delete an enrollment"""
    enrollment = Enroll.objects.get(id=enroll_id)  # Get the enrollment record by ID
    enrollment.delete()  # Delete the record from the database
    return redirect('ganji:show_enrollment')  # Redirect back to the enrollment list view