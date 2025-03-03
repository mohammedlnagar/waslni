from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm, UserProfileUpdateForm, CustomUserUpdateForm
from .models import UserProfile, CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/register.html', {'form': form})

# AJAX Username & Email Validation
def validate_registration(request):
    field = request.GET.get("field")
    value = request.GET.get("value")

    if not field or not value:
        return JsonResponse({"valid": False, "message": "Invalid request."}, status=400)

    response = {"valid": True}

    if field == "username" and CustomUser.objects.filter(username=value).exists():
        response = {"valid": False, "message": "This username is already taken."}
    elif field == "email" and CustomUser.objects.filter(email=value).exists():
        response = {"valid": False, "message": "This email is already registered."}

    return JsonResponse(response)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            
            user = form.get_user()
            login(request, user)
            print(user.email_user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    profile = request.user.profile  # Access related profile
    return render(request, 'account/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = CustomUserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = CustomUserUpdateForm(instance=user)
        profile_form = UserProfileUpdateForm(instance=profile)

    return render(request, 'account/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
