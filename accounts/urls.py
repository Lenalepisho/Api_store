from django.urls import path
from . import views


# Application namespace for reversing URLs from templates (e.g. 'accounts:login')
app_name = 'accounts'

# URL patterns for the accounts app
urlpatterns = [
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
]