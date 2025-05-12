from django.shortcuts import render, redirect
from .models import Website
from .utils import start_website_opener_thread

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            website = Website.objects.create(url=url)
            start_website_opener_thread(website.id)  # شروع ترد
            return redirect('index')
    
    websites = Website.objects.all()
    return render(request, 'index.html', {'websites': websites})