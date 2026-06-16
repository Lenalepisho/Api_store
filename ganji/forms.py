from django import forms

from .models import Enroll

COURSE_CHOICES = [
    ('', 'Choose a course...'),
    ('web-development', 'Full Stack Web Development'),
    ('data-science', 'Data Science & Analytics'),
    ('digital-marketing', 'Digital Marketing Mastery'),
    ('ui-ux-design', 'UI/UX Design Fundamentals'),
    ('cybersecurity', 'Cybersecurity Essentials'),
    ('mobile-development', 'Mobile App Development'),
    ('artificial-intelligence', 'Artificial Intelligence'),
    ('machine-learning', 'Machine Learning with Python'),
    ('social-media-marketing', 'Social Media Marketing'),
    ('graphic-design', 'Graphic Design Mastery'),
]

EDUCATION_CHOICES = [
    ('', 'Select your education level...'),
    ('high-school', 'High School'),
    ('associate', 'Associate Degree'),
    ('bachelor', "Bachelor's Degree"),
    ('master', "Master's Degree"),
    ('doctorate', 'Doctorate'),
    ('other', 'Other'),
]

EXPERIENCE_CHOICES = [
    ('', 'Select your experience...'),
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('expert', 'Expert'),
]

SCHEDULE_CHOICES = [
    ('weekdays', 'Weekdays (Monday - Friday)'),
    ('weekends', 'Weekends (Saturday - Sunday)'),
    ('flexible', 'Flexible (Self-paced)'),
]


class EnrollForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    terms = forms.BooleanField(
        required=True,
        label='I agree to the Terms of Service and Privacy Policy',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    newsletter = forms.BooleanField(
        required=False,
        label='I would like to receive course updates and educational content via email',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    select_course = forms.ChoiceField(
        required=True,
        choices=COURSE_CHOICES,
        label='Select Course',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    what_motivates_you_to_take_this_course = forms.CharField(
        required=False,
        label='What motivates you to take this course?',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    experience_level = forms.ChoiceField(
        required=False,
        choices=EXPERIENCE_CHOICES,
        label='Experience Level',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    education_level = forms.ChoiceField(
        required=False,
        choices=EDUCATION_CHOICES,
        label='Education Level',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    preferred_learning_schedule = forms.ChoiceField(
        required=False,
        choices=SCHEDULE_CHOICES,
        label='Preferred Learning Schedule',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Enroll
        fields = [
            'email',
            'select_course',
            'phone_number',
            'what_motivates_you_to_take_this_course',
            'experience_level',
            'education_level',
            'preferred_learning_schedule',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'select_course': forms.Select(attrs={'class': 'form-select'}),
        }

    def save(self, commit=True):
        enrollment = super().save(commit=False)
        first_name = self.cleaned_data.get('first_name', '').strip()
        last_name = self.cleaned_data.get('last_name', '').strip()
        enrollment.name = f"{first_name} {last_name}".strip()
        enrollment.i_agree = self.cleaned_data.get('terms', False)
        enrollment.i_would_like_to_receive_updates = self.cleaned_data.get('newsletter', False)
        if commit:
            enrollment.save()
        return enrollment
