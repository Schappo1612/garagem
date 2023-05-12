from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet, AcessorioViewSet, CorViewSet, MarcaViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"cor", CorViewSet)
router.register(r"marca", MarcaViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]