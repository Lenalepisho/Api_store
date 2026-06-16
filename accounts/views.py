from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    """Register a new user.

    Supports two template styles:
    - a plain HTML template that posts `name,email,username,password,confirm`
    - a Django `UserCreationForm` (fallback)
    """
    if request.method == 'POST':
        # If the template posts raw fields (name/email/username/password/confirm)
        if 'name' in request.POST or 'confirm' in request.POST:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '')
            confirm = request.POST.get('confirm', '')

            ctx = {'name': name, 'email': email, 'username': username}

            if not all([name, email, username, password, confirm]):
                messages.error(request, 'Please fill out all fields.')
                return render(request, 'accounts/register.html', ctx)
            if password != confirm:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'accounts/register.html', ctx)
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return render(request, 'accounts/register.html', ctx)
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            # Store full name in first_name (optional)
            user.first_name = name[:30]
            user.save()
            messages.success(request, 'Account created successfully.')
            # Log the user in
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('ganji:index')
            return redirect('ganji:index')

        # Fallback: handle Django's UserCreationForm
        form = UserCreationForm(request.POST)
        for f in form.fields.values():
            f.widget.attrs.update({'class': 'form-control'})
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request, f"Account created for {username}.")
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('ganji:index')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the errors below.')

    # GET / initial display: prefer the Django form for nicer widgets
    form = UserCreationForm()
    for f in form.fields.values():
        f.widget.attrs.update({'class': 'form-control'})
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    """Display login page and authenticate users on POST."""
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        user = authenticate(request, username=Username, password=Password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('ganji:index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')