from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic import UpdateView

# Create your views here.
from klony.forms import LoginForm
from klony.models import Acers


class LoginView2(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'klony/login_form.html', {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['login']
            pwd = form.cleaned_data['password']
            user = authenticate(username=usr, password=pwd)

            if user is not None:
                login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                else:
                    return redirect('/admin/')
            else:
                return render(request, 'klony/login_form.html', {"form": form})
        else:
            return render(request, 'klony/login_form.html', {"form": form})


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
            return redirect('/login')
        else:
            pass


class AcerUpdate(UpdateView):
    model = Acers
    fields = ['botanic_name', 'latin_name', 'image_tree', 'new_image_tree', 'new_image_bark', 'new_image_leaf']
    template_name_suffix = '_form'
    success_url = '#'


class AcerList(ListView):
    model = Acers
    fields = ['botanic_name', 'latin_name', 'image_tree', 'new_image_tree', 'new_image_bark', 'new_image_leaf']
    # template_name_suffix = '_form'
    # success_url = '#'
