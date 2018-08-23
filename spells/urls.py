from django.conf.urls import url
from . import views

app_name = 'spells'

urlpatterns = [
    url(r'^$', views.spell_list, name="list"),
    url(r'^create/$', views.spell_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.spell_detail, name="detail"),
]
