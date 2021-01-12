from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myapp.forms import signupForm
# Create your views here.
def home_view(request):
	return render(request,'myapp/home.html')
@login_required
def java_view(request):
	return render(request,'myapp/javaexams.html')
@login_required
def python_view(request):
	return render(request,'myapp/pythonexams.html')
@login_required
def aptitude_view(request):
	return render(request,'myapp/aptitudeexams.html')
def logout_view(request):
	return render(request,'myapp/logout.html')
def signup_view(request):
	f=signupForm()
	if request.method=='POST':
		f=signupForm(request.POST)
		user=f.save()
		user.set_password(user.password)
		user.save()
		return redirect("/accounts/login")
	d={"form":f}
	return render(request,'myapp/signup.html',d)
	