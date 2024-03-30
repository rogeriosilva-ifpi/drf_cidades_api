from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .viewsets import (
    EstadoViewSet,
    CidadeViewSet,
    SignupAPIView,
)

# Roteador
router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'signup', SignupAPIView)

estado_router = routers.NestedDefaultRouter(
    router, r'estados', lookup='estado')
estado_router.register(r'cidades', CidadeViewSet,
                       basename='estado-cidades')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(estado_router.urls)),
    # path('signin', ObtainAuthToken.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
