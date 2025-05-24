from django.urls import path

from home import views

app_name = 'home' # espacio de nombre para url

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]