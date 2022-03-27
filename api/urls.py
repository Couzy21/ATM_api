from django.urls import path
from .views import AccountList,AccountDetail


urlpatterns = [
path('<int:pk>/', AccountDetail.as_view()),
path('', AccountList.as_view()),
]