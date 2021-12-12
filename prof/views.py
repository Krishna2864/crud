from django.shortcuts import render , redirect
from .models import Pro , Userpro
from .form import Pro
# Create your views here.
def home(request):
    form = Pro()
    if request.method == 'POST':
        form = Pro(request.POST)
        if form.is_valid():
            form.save()
            c = Userpro.objects.all()
            return render(request, 'prof/h.html', {'c': c})




    return  render(request,'prof/home.html',{'form':form})



