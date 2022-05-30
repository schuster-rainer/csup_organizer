from django.shortcuts import  render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

def register_request(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})