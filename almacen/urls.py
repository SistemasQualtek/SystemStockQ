from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    AlmacenList,
    AlmacenDetail,
    AlmacenCreation,
    AlmacenUpdate,
    AlmacenDelete
)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    ###################### Urls Almacenes ######################
    url(r'^AlmacenList/$', AlmacenList,name='list_almacen'),
    url(r'^Almacen/(?P<pk>[0-9]+)/$', views.AlmacenDetail, name='detail_almacen'),
    url(r'^Almacen/nuevo',views.AgregaraStock,name="almacen"),
    url(r'^editar_almacen/(?P<pk>\d+)', login_required(AlmacenUpdate.as_view()), name='edit_almacen'),
    url(r'^borrar_almacen/(?P<pk>\d+)', login_required(AlmacenDelete.as_view()), name='delete_almacen'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
