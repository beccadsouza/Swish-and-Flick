from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from spells import views as spells_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^spells/', include('spells.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', spells_view.spell_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
