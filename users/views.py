from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render_to_response
from .models import UploadForm,Upload
from .forms import CustomUserCreationForm

# Create your views here.

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

def edit_names(request):
	template_name="edit_names.html"
	if request.method == "POST":
		form = CustomUserCreationForm(data=request.POST, instance=request.user)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			url = reverse('home')
			return HttpResponseRedirect(url)
	else:
		form = CustomUserCreationForm(instance=request.user)
	page_title = ('Edit user names')
	return render(request, template_name, {'form': form})

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