from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils import timezone

from .forms import UserForm

def login(request):
    # if this is a POST request we need to process the form data
    #del request.session['member_id']
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            # get post information from user
            _email = form.cleaned_data['Input_Email']
            _password = form.cleaned_data['Input_Password']
            # identify user from admin db
            user = authenticate(username= _email, password= _password)

            if user is not None:
                conection = "l'utilisateur existe"
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                request.session['member_id'] = _email
                print(conection)
            else:
                conection = "l'utilisateur n'existe pas"
                print(conection)

            return render(request, 'polls/login.html', {'form': conection})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'polls/login.html', {})

def account(request):

    return render(request, 'polls/account.html', {})
