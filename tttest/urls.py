from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from tttest import views

urlpatterns = [
    url(r'^miya', views.page_not_found, name='miya'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
