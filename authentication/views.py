from django.shortcuts import render, redirect
from authentication import forms
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        custom_user_form = forms.CustomUserForm(request.POST, request.FILES)

        if custom_user_form.is_valid():
            custom_user = custom_user_form.save()
            custom_user.save()

            login(request, custom_user)
            return redirect('/')  
        
    else:
        custom_user_form = forms.CustomUserForm() 

    return render(request, 'authentication/register.html', {'custom_user_form': custom_user_form})

def logout_view(request):
    logout(request)
    return redirect('/')  

def change_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        if new_username:
            request.user.username = new_username
            request.user.save()
            messages.success(request, 'Имя пользователя успешно изменено.')
            return redirect('settings')
    return render(request, 'authentication/change_username.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Аккаунт успешно удалён.')
        return redirect('/')
    return render(request, 'authentication/delete_account.html')
