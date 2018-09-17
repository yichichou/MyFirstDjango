
from django.conf.urls import url
# Import view functions from trips app.
from . import views

#url(regex, view)
urlpatterns = [
	url(r'^$', views.frontpage),
    url(r'^settings/$',views.settings),	
    url(r'^add_category$',views.addCategory),
    url(r'^delete_category/(?P<category>\w+)',views.deleteCategory),'''這邊的category為一個參數傳入的名稱'''
    
]
