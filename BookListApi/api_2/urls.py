from . import views
from django.urls import path
# from views import BookModelVset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', views.BookModelVset)
# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     path('books/', views.books),
#     path('books/<int:pk>', views.book_info),
# ]