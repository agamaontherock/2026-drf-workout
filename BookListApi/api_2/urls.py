from . import views
from django.urls import path, include
from rest_framework import urls
# from views import BookModelVset
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'books', views.BookModelVset)
# router.register(r'accounts', AccountViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('books/<int:pk>', views.book_info),
    path('genres/<int:pk>', views.genre_info, name="genre-detail"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


