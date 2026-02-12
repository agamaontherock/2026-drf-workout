from . import views
from django.urls import path, include
# from views import BookModelVset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', views.BookModelVset)
# router.register(r'accounts', AccountViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('books/<int:pk>', views.book_info),
    path('genres/<int:pk>', views.genre_info, name="genre-detail"),
]