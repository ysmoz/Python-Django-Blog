from django.contrib import messages
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
from blog.models import Blog, Category
from home.models import Setting, ContactFormMessage, ContactFormu


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Blog.objects.all()[:3]
    category=Category.objects.all()
    context = {'setting': setting, 'page':'home','sliderdata':sliderdata,'category':category}
    return render(request, 'index.html', context)

def hakkimda(request):
    setting=Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'category':category}
    return render(request, 'hakkimda.html', context)

def referanslarimiz(request):
    setting=Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page':'referanslarimiz','category':category}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    if request.method== 'POST':
        form =ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"MesajÄ±nÄ±z baÅŸarÄ±lÄ± ÅŸekilde gÃ¶nderilmiÅŸtir.TeÅŸekkÃ¼r ederiz")
            return  HttpResponseRedirect('/iletisim')

    setting=Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,'form':form,'category':category}
    return render(request, 'iletisim.html', context)