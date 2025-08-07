import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise, Useful_Materials
from .forms import ExercisesForm
from django.conf import settings
from django.core.paginator import Paginator

def sport_exercises_view(request):
    exercise = Exercise.objects.all()
    return render(request, 'exercises/sport_exercises.html', {'exercises': exercise})

@login_required
def my_exercises_view(request):
    if request.method == 'POST':
        form = ExercisesForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect('my_exercises')
    else:
        form = ExercisesForm()

    
    exercises = Exercise.objects.filter(user=request.user)

    return render(request, 'exercises/my_exercises.html', {
        'form': form,
        'exercises':exercises
    })

def video_gallery(request):
    folder_path = os.path.join(settings.MEDIA_ROOT, 'exercise_videos')
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
    video_urls = [f"{settings.MEDIA_URL}exercise_videos/{name}" for name in file_names]
    paginator = Paginator(video_urls, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'exercises/video_gallery.html', {'page_obj': page_obj})