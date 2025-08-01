from django.shortcuts import redirect, render
from authentication import forms
from django.contrib.auth import login, logout
from .forms import WeightUpdateForm

def register(request):
    if request.method == 'POST':
        custom_user_form = forms.CustomUserForm(request.POST, request.FILES)

        if custom_user_form.is_valid():
            custom_user = custom_user_form.save()
            custom_user.save()

            login(request, custom_user)
            return redirect('main')  
        
    else:
        custom_user_form = forms.CustomUserForm() 

    return render(request, 'authentication/register.html', {'custom_user_form': custom_user_form})

def logout_view(request):
    logout(request)
    return redirect('/')  

# Обновление веса 

def update_weight(request):
    user = request.user
    if request.method == 'POST':
        form = WeightUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WeightUpdateForm(instance=user)

    return render(request, 'account/update_weight.html', {'form': form})