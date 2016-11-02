from django.http import HttpResponse, HttpResponseRedirect
from models import UserForm, User
from django.shortcuts import render


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            User.objects.create(
                name=name,
                email=email,)
            # redirect to a new URL:
            return HttpResponseRedirect('/users/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'users/index.html', {'form': form})

def thanks(request):
    return HttpResponse("User added.")
