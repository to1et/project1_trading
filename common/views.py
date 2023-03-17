from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserCreationForm
from .models import User
from .forms import UserChangeForm
from django. contrib.auth.decorators import login_required

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required(login_url='common:login')
def userinfo(request):
    """
    유저 정보
    """
    return render(request, 'common/userinfo.html')


@login_required(login_url='common:login')
def userinfo_modify(request):
    """
    유저 정보 수정
    """

    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # user = form.save(commit=False)
            # user.save()
            return redirect('index')
    else:
        form = UserChangeForm(instance=request.user)

    context = {'form':form}
    return render(request, 'common/userinfo_modify.html', context)

