

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from audit import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('audit/', include('audit.urls')), 
    path('avto_cc/', include('avto_cc.urls')),
    path('avto_bs/', include('avto_bs.urls')),
    path('api/v1/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    
]
