from django.db import models

# Create your models here.
class Enroll(models.Model):
    """This enrollment table stores information about student enrollments in courses."""
    name=models.CharField(max_length=100)  # Student's name
    email=models.EmailField()  # Student's email address
    select_course=models.CharField(max_length=100)  # Course name the student is enrolling in
    phone_number=models.CharField(max_length=20)  # Student's contact number
    what_motivates_you_to_take_this_course=models.TextField()  # Additional message or comments from the student
    experience_level=models.CharField(max_length=100)  # Student's experience level or background
    education_level=models.CharField(max_length=100)  # Student's educational background
    preferred_learning_schedule=models.CharField(max_length=100)  # Student's preferred learning schedule
    i_agree=models.BooleanField()  # Indicates whether the student agrees to terms and conditions
    i_would_like_to_receive_updates=models.BooleanField()  # Indicates whether the student wants to receive updates
    
    def __str__(self):
        """String representation of the enrollment object."""
        return f"{self.name} enrolled in {self.select_course}"