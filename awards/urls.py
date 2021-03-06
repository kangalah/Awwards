"""awards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views
from rest_framework import routers
from awwwwards import views as view
from awwwwards.views import ProfileViewSet,PostViewSet
from rest_framework.authtoken.views import obtain_auth_token




router = routers.DefaultRouter()
router.register(r'profiles',view.ProfileViewSet)
router.register(r'posts', view.PostViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include(router.urls)),
    url(r'',include('awwwwards.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^logout/$',views.logout, {"next_page":'/'},name="logout"),
    url(r'^api-token-auth/', obtain_auth_token),
    
]