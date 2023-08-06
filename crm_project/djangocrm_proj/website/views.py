from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def func(request):
    records = Record.objects.all()


    # Check to see if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Logged In")
            return redirect('Home')
        else:
            messages.success(request,"There was an error logging in try again")
            return redirect('Home')
    else:
        return render(request, 'Home.html',{'records':records})





def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out....")
    return redirect('Home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('Home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('Home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('Home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('Home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('Home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('Home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('Home')

def ham(request):
    return HttpResponse("HELLO THERE")


def home1(request):
    path = request.path
    return HttpResponse(path,content_type='text/html',charset='utf-8')


def h1(request):
    response = HttpResponse("This Works !")
    return response


def func2(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 22

    msg = f"""<br>
        <br>Path:{path}
        <br>Address:{address}
        <br>Scheme:{scheme}
        <br>Method:{method}
        <br>User Agent:{user_agent}
        <br>Path info:{path_info}
        <br>Response Header:{response.headers}
        
    """

    return HttpResponse(msg,content_type='text/html',charset='utf-8')



def menuitems(request,dish) :
       items = {
        'Pasta': 'Pasta is a type of noodles made from combinations',
        'falafel': 'arabic dish made of beans',
        'cheesecake': 'Desert'
       }

       description = items[dish]
       return HttpResponse(f"<h1>{dish}</h1>" + description)
       


     