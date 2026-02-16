from django.shortcuts import render, redirect
from apps.shops_app.forms import LoginForm, UserForm
from apps.shops_app.forms import User
from apps.shops_app.services.decorators import logout_def
from django.contrib.auth.hashers import check_password


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            forma_user = form.cleaned_data.get("username")
            forma_password = form.cleaned_data.get("password")
            try:
                baza_user = User.objects.get(username=forma_user)
                if check_password(forma_password, baza_user.password): # BU TO'G'RI
                    request.session["user_id"] = baza_user.id
                    next_url = request.GET.get('next', '/')
                    return redirect(next_url)
            except User.DoesNotExist:
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, "forms/login.html", {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Bazaga darrov saqlama
            user.set_password(form.cleaned_data['password'])  # Parolni shifrlaydi!
            user.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserForm()

    return render(request, 'forms/register.html', {'form': form})


def logout_page(request):
    logout_def(request)
    return redirect("main_page")
