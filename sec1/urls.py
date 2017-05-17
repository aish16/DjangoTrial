from django.conf.urls import url
from .import views

urlpatterns =[
url(r'^(?P<Department_id>[0-9]+)/$',views.dept, name='dept'),    
url(r'^$',views.index, name='index'),

]
