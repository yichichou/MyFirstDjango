
from django.conf.urls import url
# Import view functions from trips app.
from . import views

#url(regex, view)
urlpatterns = [
	url(r'^$', views.frontpage),	
]
