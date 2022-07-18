from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created')
            return redirect('login')
        else:
            messages.warning(request, 'Enter correct information')
    form = UserRegistrationForm()
    return render (request, 'users/register.html',
    {
        'form': form,
        'title': 'Register'
    })

@login_required
def profile(request):
    return render(request, 'users/profile.html')
