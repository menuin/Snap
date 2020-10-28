from django.shortcuts import render, get_object_or_404
from .forms import NameForm
from core.models import Couple
from django.shortcuts import redirect

def home(request):
    return render(request, 'core/home.html')

def moving_in(request):
    form=NameForm()
    """ if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            couple=form.save(commit=False)
            couple.save()
            return redirect('home')
        else:
            form=NameForm()
    else:
        form=NameForm() """
    return render(request,'core/movingin.html',{'form':form})




def 반갈죽(request):
    return render(request, 'core/bangal.html',)

# Create your views here.
