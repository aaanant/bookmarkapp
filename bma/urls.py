from django.conf.urls import url
from . import views
urlpatterns = [ url(r'^user/(?P<username>[-\w]+)/$',views.bookmark_user, name= 'bma_bookmark_user'),url(r'^$', views.bookmark_list, name='bma_bookmark_list'),]


