from django.urls import path
from . import views

app_name = 'ganji'
urlpatterns = [
    path('', views.home, name='index'),  # path to the home view (named index for templates)
    path('about/', views.about, name='about'),  # path to the about view
    path('courses/', views.courses, name='courses'),  # path to the courses view
    path('enroll/', views.enroll, name='enroll'),  # path to the enroll view
    path('contact/', views.contact, name='contact'),  # path to the contact view
    path('instructors/', views.instructors, name='instructors'),  # path to the instructors view
    path('pricing/', views.pricing, name='pricing'),  # path to the pricing
    path('blog/', views.blog, name='blog'),  # path to the blog view
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),  # path to the course detail view
    path('show_enrollment/', views.read_enroll, name='show_enrollment'),  # path to the view that displays all enrollments 
    path('delete_enrollment/<int:enroll_id>/', views.delete_enroll, name='delete_enrollment'),  # path to the view that deletes an enrollment
    path('update_enrollment/<int:enroll_id>/', views.update_enroll, name='update_enrollment'),  # path to the view that updates an enrollment
   
    
]
