from django.shortcuts import render, redirect
from .forms import WeightUpdateForm
from .models import WeightEntry
from .forms import WeightEntryForm
from django.contrib.auth.decorators import login_required

def update_weight(request):
    user = request.user
    if request.method == 'POST':
        form = WeightUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WeightUpdateForm(instance=user)

    return render(request, 'weight/update_weight.html', {'form': form})


@login_required
def weight_tracker(request):
    form = WeightEntryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        return redirect('weight_tracker')

    entries = WeightEntry.objects.filter(user=request.user).order_by('date')
    dates = [entry.date.strftime('%Y-%m-%d') for entry in entries]
    weights = [entry.weight for entry in entries]

    return render(request, 'weight/weight_tracker.html', {
        'form': form,
        'dates': dates,
        'weights': weights
    })
