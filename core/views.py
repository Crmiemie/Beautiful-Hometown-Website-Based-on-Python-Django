from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import logout, update_session_auth_hash

from core.forms import SignupForm, NewMoment, NewItemForm
from core.models import Information, Location_Pic, City_Feature, Moment


# Create your views here.

def index(request):
    query = request.GET.get('query', '')
    if query:
        detail = City_Feature.objects.filter(city_name=query)
        city_url = Location_Pic.objects.filter(name=query)[0].image.url
        city_description = Location_Pic.objects.filter(name=query)[0].description

        return render(request, 'core/showcity.html', {
            'city_name': query,
            'city_url': city_url,
            'city_des': city_description,
            'features': detail,
        })
    else:
        return render(request, 'core/index.html')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            user = User.objects.get(username=request.user.username)
            user.set_password(not request.POST.get('old_password'))
            return redirect('core:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'core/pchan.html', {
        'form': form
    })



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('core:information')

    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
    })


def information_filled(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('core:login')
    else:
        form = NewItemForm()
    return render(request, 'core/information.html', {
        'form': form,
    })


def logout_view(request):
    logout(request)
    return render(request, 'core/index.html')


@login_required
def city_show(request):
    username = request.user.username
    information = Information.objects.filter(name=username)[0]
    city = information.city
    city_url = Location_Pic.objects.filter(name=city)[0].image.url
    city_description = Location_Pic.objects.filter(name=city)[0].description
    detail = City_Feature.objects.filter(city_name=city)
    print(city_url)
    return render(request, 'core/showcity.html', {
        'city_name': city,
        'city_url': city_url,
        'city_des': city_description,
        'features': detail,
    })


def moment(request):
    if request.method == 'POST':
        form = NewMoment(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.belongs_to = request.user
            item.save()

            return redirect('core:moment')
    else:
        form = NewMoment()

    moments = Moment.objects.filter(belongs_to=request.user)

    return render(request, 'core/moment.html', {
        'form': form,
        'moments': moments,
    })


def edit_moment(request, pk):
    if request.method == 'POST':
        form = Moment.objects.filter(id=pk)[0]
        form.title = request.POST['title']
        form.note = request.POST['note']
        # form.image = request.POST.get('new_ima')
        form.save()
        return redirect('core:moment')
    else:

        form1 = Moment.objects.get(id=pk)
        form = NewMoment(instance=form1)
    return render(request, 'core/edit_moment.html', {
        'form' : form,
    })

def delete_moment(request, pk):
    Moment.objects.filter(id=pk).delete()
    return redirect('core:moment')


