import functools, operator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic import UpdateView

# Create your views here.
from klony.forms import LoginForm, AcersSearchForm
from klony.models import Acers, SHAPES1, FROST_RES, COLORS

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
    success_url = '/acer/'


class AcerList(ListView):
    model = Acers
    fields = ['uid', 'botanic_name', 'latin_name', 'image_tree', 'new_image_tree', 'new_image_bark', 'new_image_leaf']
    # success_url = '#'

def search_acers_objects(b_uid, l_uid, shape, frost, lc_summer, lc_autumn):
    acers = list()
    acers_obj = list()
    if b_uid:
        acers_obj.append(Acers.objects.get(pk=b_uid))
    elif l_uid:
        acers_obj.append(Acers.objects.get(pk=l_uid))
    else:
        acers_obj = Acers.objects.all()
        if shape:
            acers_obj = acers_obj.filter(shape1=shape)
        if frost:
            acers_obj = acers_obj.filter(frost_res=frost)
        if lc_summer:
            acers_obj = acers_obj.filter(lc_summer1=lc_summer)
        if lc_autumn:
            acers_obj = acers_obj.filter(lc_autumn1=lc_autumn)


    for a in acers_obj:
        d = dict()
        d['uid'] = a.uid
        d['botanic_name'] = a.botanic_name
        d['latin_name'] = a.latin_name
        d['new_image_tree'] = a.new_image_tree
        d['new_image_bark'] = a.new_image_bark
        d['new_image_leaf'] = a.new_image_leaf
        acers.append(d)

    return acers


class AcerSearch(View):
    def get(self, request):
        form = AcersSearchForm()
        acers = list()
        acers_obj = Acers.objects.all()

        for a in acers_obj:
            d = dict()
            d['uid'] = a.uid
            d['botanic_name'] = a.botanic_name
            d['latin_name'] = a.latin_name
            # d['shape1'] = dict(SHAPES1).get(a.shape1)
            acers.append(d)
        # d = dict(SHAPES1)
        # acers['shape1'].append(dict(SHAPES1))
        # shapes_tmp = list(SHAPES1)
        # shapes = list()
        # for i in shapes_tmp:
        #     shapes.append(i[0])
        return render(request,
                      'klony/acers_search.html',
                      {'acers': acers,
                       'ashapes': SHAPES1,
                       'frost': FROST_RES,
                       'lc_summer': COLORS,
                       'lc_autumn': COLORS
                       }
                      )

    def post(self, request):
        form = AcersSearchForm(request.POST)
        acers = list()
        if form.is_valid():
            # bname = form.cleaned_data['botanic_name']
            # lname = form.cleaned_data['latin_name']
            b_uid = form.cleaned_data['b_uid']
            l_uid = form.cleaned_data['l_uid']
            shape = form.cleaned_data['shape']
            frost = form.cleaned_data['frost']
            lc_summer = form.cleaned_data['lc_summer']
            lc_autumn = form.cleaned_data['lc_autumn']
            acers = search_acers_objects(b_uid, l_uid, shape, frost, lc_summer, lc_autumn)

        return render(request,
                      'klony/acers_search.html',
                      {'acers': acers})


class AcerHome(View):
    def get(self, request):
        return render(request,
                      'klony/acers_home.html',
                      )


class AcerCultivation(View):
    def get(self, request):
        return render(request,
                      'klony/acers_cultivation.html',
                      )
