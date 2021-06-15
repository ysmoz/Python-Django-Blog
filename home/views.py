from django.contrib import messages
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu


def index(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)

def hakkimda(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimda.html', context)

def referanslarimiz(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'referanslarimiz'}
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
            messages.success(request,"Mesajınız başarılı şekilde gönderilmiştir.Teşekkür ederiz")
            return  HttpResponseRedirect('/iletisim')

    setting=Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,'form':form}
    return render(request, 'iletisim.html', context)