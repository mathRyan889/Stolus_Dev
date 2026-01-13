from django.shortcuts import render, redirect
from .forms import LeadForm

def home(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LeadForm()

    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')
