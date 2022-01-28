from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import Another
from .views import BookCount
from .views import BookList
from .views import BookListPublished
from .views import Book2
from .views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first', views.first),
    path('first_template', views.first_template),
    path('dynamic_template', views.dynamic_template),
#    path('another', Another.as_view()),
    path('bookcount', BookCount.as_view()),
    path('booklist', BookList.as_view()),
    path('booklistpublished', BookListPublished.as_view()),
    path('book2', Book2.as_view()),
]
