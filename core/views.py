from django.shortcuts import render, get_object_or_404
from .forms import MoveForm
from core.models import Couple
from django.db import models
from django.shortcuts import redirect
from django.utils import timezone
import random

def home(request):
    couples=Couple.objects.all()
    return render(request, 'core/home.html',{'couples':couples})

def couple_main(request,pk):
    couple=get_object_or_404(Couple,pk=pk)
    return render(request,'core/detail',{'couple':couple})

def moving_in(request):
    if request.method=='POST':
        form=MoveForm(request.POST, request.FILES)
        if form.is_valid():
            couple=form.save(commit=False)
            couple.created_date=timezone.now()
            couple.save()
        return redirect('home')
    else:
        form=MoveForm()
    return render(request,'core/movingin.html',{'form':form})

def love_love(request,pk):
    couple=get_object_or_404(Couple,pk=pk)
    couple.love+=1
    couple.save()
    return render(request,'core/detail.html',{'couple':couple})

def snap(request,pk):
    couple=get_object_or_404(Couple,pk=pk)
    couple.choice=random.randint(0,1)
    couple.snapped=1
    couple.love=0
    # couple.photo='/media/core/images/policeline.jpg'
    couple.save()
    return render(request,'core/snap.html',{'couple':couple})

def moving_out(request,pk):
    couple=get_object_or_404(Couple,pk=pk)
    couple.delete()
    couples=Couple.objects.all()
    return render(request,'core/home.html',{'couples':couples})

def suspect(request,pk):
    couple=get_object_or_404(Couple,pk=pk)
    couple.delete()
    couples=Couple.objects.all()
    return render(request,'core/suspect.html',{'couples':couples})

# Create your views here.
