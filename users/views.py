from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import UploadForm,Upload
from .forms import CustomUserCreationForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)       
        if img.is_valid():
            img.save()  
            return HttpResponseRedirect(reverse('home'))
    else:
        img=UploadForm()
    images=Upload.objects.all()
    return render(request,'home.html',{'form':img,'images':images})