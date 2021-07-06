from django.shortcuts import render
from .models import *
# Create your views here.
def views():
	view ={}
	view["feedback"]=Feedback.objects.all()
	return view


	return render(request,'index.html',view)
def home(request):
	view=views()


	return render(request,'index.html',view)

def about(request):
	view=views()

	return render(request,'about.html',view)

def contact(request):
	status={}
	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']
		data=Contact.objects.create(
			name=name,
			email=email,
			subject=subject,
			message=message
			)
		data.save()
		status={}
		status['message']='form is submitted'

	return render(request,'contact.html',status)

def portfolio(request):

	return render(request,'portfolio.html')

def price(request):

	return render(request,'price.html')

def services(request):

	return render(request,'services.html')