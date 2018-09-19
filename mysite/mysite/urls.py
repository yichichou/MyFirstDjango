"""mysite URL Configuration

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
# Import view functions from trips app.
from trips import views
from django.contrib.auth import views as auth_views

#url(regex, view)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^hello/$', views.hello_world), #regex:代表的是 hello/ 這種 URL  #hello_world 這個 view的function
	#url(r'^echo/(?P<userid>[0-9]+)$', views.echo),
	url(r'^echo/$', views.echo),
    url(r'^home/$', views.home),

    #Django範例教學用↓
	url(r'', include('trips.urls')),
    url(r'^accounts/login',auth_views.login),
    url(r'^accounts/logout', views.logout),
	
]
