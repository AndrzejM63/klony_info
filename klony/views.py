import functools, operator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic import UpdateView

# Create your views here.
from klony.forms import LoginForm, AcersSearchForm, AcersSingleForm
from klony.models import Acers, ORIGIN, SHAPES1, FROST_RES, COLORS
from klony_info.settings import MEDIA_URL


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


class AcerList(View):
    def get(self, request):
        acers = search_acers_objects()
        acersEu = list()
        acersAs = list()
        acersNa = list()
        for a in acers:
            if a['origin1'] == 'EU':
                acersEu.append(a)
            elif a['origin1'] == 'AS':
                acersAs.append(a)
            elif a['origin1'] == 'NA':
                acersNa.append(a)

        return render( request, 'klony/acers_list.html',
                       {'acersEu': acersEu,
                       'acersAs': acersAs,
                       'acersNa': acersNa}
                       )


def search_acers_objects(b_uid='', l_uid='', shape='', frost='', lc_summer='', lc_autumn=''):
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
        d['other_names'] = a.other_names
        d['latin_name'] = a.latin_name
        d['description'] = a.description
        d['origin1'] = a.origin1
        d['image_tree'] = a.image_tree
        acers.append(d)

    return sorted(acers, key=lambda k: k['botanic_name'].lower())


class AcerSearch(View):
    def get(self, request):
        form = AcersSearchForm()
        acers = list()
        acers_obj = Acers.objects.all()

        for a in acers_obj:
            d = dict()
            d['uid'] = a.uid
            d['botanic_name'] = a.botanic_name + ' ' + a.variant
            d['latin_name'] = a.latin_name + ' ' + a.variant
            acers.append(d)
        acers_lat = sorted(acers, key=lambda k: k['latin_name'].lower())
        acers_bot = sorted(acers, key=lambda k: k['botanic_name'].lower())
        return render(request,
                      'klony/acers_search.html',
                      {'acers_bot': acers_bot,
                       'acers_lat': acers_lat,
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
            b_uid = form.cleaned_data['b_uid']
            l_uid = form.cleaned_data['l_uid']
            shape = form.cleaned_data['shape']
            frost = form.cleaned_data['frost']
            lc_summer = form.cleaned_data['lc_summer']
            lc_autumn = form.cleaned_data['lc_autumn']
            acers = search_acers_objects(b_uid, l_uid, shape, frost, lc_summer, lc_autumn)
        acersEu = list()
        acersAs = list()
        acersNa = list()
        for a in acers:
            if a['origin1'] == 'EU':
                acersEu.append(a)
            elif a['origin1'] == 'AS':
                acersAs.append(a)
            elif a['origin1'] == 'NA':
                acersNa.append(a)

        return render(request,
                      'klony/acers_list.html',
                      {'acersEu': acersEu,
                       'acersAs': acersAs,
                       'acersNa': acersNa}
                      )


class AcerDetails(View):
    def get(self, request, pk):
        # p = Acers.objects.get(pk=pk)
        p = get_object_or_404(Acers, pk=pk)
        if p is None:
            return render(request, 'klony/acers_home.html')
        else:
            d = dict( botanic_name_variant=p.botanic_name + ' ' + p.variant,
                     other_names=p.other_names, latin_name=p.latin_name,
                     description=p.description,
                     origin=dict(ORIGIN).get(p.origin1) + ' ' + p.origin2,
                     occurrence=p.occurrence, max_height=str(p.height_max1)+' m',
                     shape=p.shape1 + ' ' + p.shape2, leaf_structure=p.leaf_structure,
                     leaf_size=p.leaf_size,
                     leaf_spring=p.lc_spring2,
                     leaf_summer=p.lc_summer2,
                     leaf_autumn=p.lc_autumn2,
                     leaf_tail=p.leaf_tail,
                     bark=p.bark, flowers=p.flowers, fruits=p.fruits,
                     frost_res=p.frost_res, frost_zone=p.frost_res_zones, stand=p.stand,
                     soil_kind=p.soil_kind, soil_ph=p.soil_ph,
                     characteristics=p.characteristics,
                     poland_availability='Nie' if p.poland_availability==0 or p.poland_availability is None else 'Tak')
            d['image_tree']= p.image_tree
            d['image_bark']=p.image_bark
            d['image_leaf']=p.image_leaf
            form = AcersSingleForm(initial=d)

        return render(request,
                      'klony/acers_details.html',
                      {'form': form,
                       'MEDIA_URL': MEDIA_URL})


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


class AcerBibliography(View):
    def get(self, request):
        return render(request,
                      'klony/acers_bibliography.html',
                      )
