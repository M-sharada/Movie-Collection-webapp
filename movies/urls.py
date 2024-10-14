from django.urls import path
from .views import (
    ApiOverviewView,
    RegisterView,
    MovieListView,
    CollectionView,
    CollectionDetailView,
    RequestCountView,
    RequestCountResetView,
    LoginView  # Custom LoginView using JWT
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', ApiOverviewView.as_view(), name='api-overview'),
    path('register/', RegisterView.as_view(), name='register'),
    
    # JWT Login and Token Refresh Endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Default JWT login
    path('api/login/', LoginView.as_view(), name='login'),  # Custom login view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh

    # Movie and Collection Endpoints
    path('movies/', MovieListView.as_view(), name='movies'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('collection/<uuid:collection_uuid>/', CollectionDetailView.as_view(), name='collection_detail'),

    # Request Count Endpoints
    path('request-count/', RequestCountView.as_view(), name='request_count'),
    path('request-count/reset/', RequestCountResetView.as_view(), name='request_count_reset'),
]
