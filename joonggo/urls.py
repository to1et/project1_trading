from django.urls import path
from . import views

app_name = 'joonggo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sell_id>/', views.detail, name='detail'),
    path('comment/create/<int:sell_id>/', views.comment_create, name='comment_create'),
    path('question/create/', views.sell_create, name='sell_create'),
]
