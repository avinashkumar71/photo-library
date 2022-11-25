from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Image
from .form import ImageForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForm()
    image = Image.objects.all()
    context = {
        'image': image,
        'form': form,
    }
    return render(request, 'home.html', context)