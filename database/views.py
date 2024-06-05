from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from database.models import Person, PersonForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    form = PersonForm()
    success_message = ""
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Successfully registered"
            return render(request, 'register.html', {'form': form, 'success_message': success_message})

    data = {'form': form}
    return render(request, 'register.html', data)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            person = Person.objects.get(username=username, password=password)
            request.session['person_id'] = person.id
            return redirect('person')
        except Person.DoesNotExist:
            return render(request, 'signin.html', {'message': 'Invalid credentials'})
    return render(request, 'signin.html')

def person(request):
    person_id = request.session.get('person_id')
    if person_id:
        person = Person.objects.get(id=person_id)
        return render(request, 'person.html', {'person': person})
    return render(request,'signin')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')
