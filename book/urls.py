from django.urls import path
from .views import BookList,BookDetail,BookCreate,BookUpdeteDelete,Bookcreate
urlpatterns = [
    path('', BookList.as_view()),
    path('<int:pk>/', BookDetail.as_view()),
    path('create/', BookCreate.as_view()),
    path('creat/',Bookcreate.as_view()),
    path('updatedelete/<int:pk>/', BookUpdeteDelete.as_view())
]