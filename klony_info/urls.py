"""klony_info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

from klony.views import AcerUpdate, LoginView2, LogoutView, AcerList, AcerSearch, AcerHome, AcerCultivation, \
    AcerBibliography

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout2/$', logout_then_login, name='site-logout'),
    url(r'^login/?$', LoginView2.as_view(), name='login-form'),
    url(r'^logout/?$', LogoutView.as_view(), name='logout-form'),
    url(r'^acer/(?P<pk>\d+)/?$', AcerUpdate.as_view(), name='acer-update'),
    url(r'^acers/?$', AcerList.as_view(), name='acer-list'),
    url(r'^acer/?$', AcerSearch.as_view(), name='acer-search'),
    url(r'^$|^home$', AcerHome.as_view(), name='acer-home'),
    url(r'^cultivation/$', AcerCultivation.as_view(), name='acer-cultivation'),
    url(r'^bibliography/$', AcerBibliography.as_view(), name='acer-bibliography'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
