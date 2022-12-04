from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from. forms import UserEditForm
from .models import UserProfile
# Create your views here.
def home(request):

    context = {}
    return render(request, 'profiles/home.html', context)


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

def upload_action(request):
    csv_file = request.FILES["csv_upload"]

    if not csv_file.name.endswith('.csv'):
        messages.warning(request, 'The wrong file type was uploaded')
        return HttpResponseRedirect(request.path_info)

    file_data = csv_file.read().decode("utf-8")
    csv_data = file_data.split("\n")

    for x in csv_data:
        fields = x.split(",")
        created = UserProfile.objects.update_or_create(
            email = fields[0],
            user_name = fields[1],
            first_name = fields[2],
            # start_date = fields[3],
            # is_staff = fields[4],
            # is_active = fields[5],
            # points = fields[6],
            # rank = fields[7],
            examNo = fields[8],
            exam_yr = fields[9],
            )
    url = reverse('admin:index')
    return HttpResponseRedirect(url)


def upload_csv(request):
    # if request.method == "post":
    form = CsvImportForm()
    context = {'form':form}
    return render(request, 'profiles/csv_upload.html', context)

def profile_detail(request, pk):
    #
    #
    user = get_object_or_404(UserProfile, pk=pk)
        
    # articles = Articles.objects.filter(bookmarked=profile.id)
    # questions = Questions.objects.filter(author=user.id)
    
    points = user.rank
    
    
    context = {'user':user, 'points':points,} # , 'image_url':image_url
    return render(request, 'profiles/profile_detail.html', context)

@login_required
def edit_profile(request):
    user = get_object_or_404(UserProfile, pk=request.user.pk)
    
    points = user.rank
    
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
    
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('profiles:edit_profile'))
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'user':user, 
        'points':points,
        'user_form':user_form,
        }
    return render(request, 'profiles/edit_profile.html', context)