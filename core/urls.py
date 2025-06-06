from django.urls import path

from core import views

app_name = 'core' # espacio de nombre para url

urlpatterns = [
    path('list/banks/', views.ListBank.as_view(), name='list_bank'),
    path('detail/bank/<int:pk>/', views.DetailBank.as_view(), name='detail_bank'),
    path('create/bank/', views.CreateBank.as_view(), name='create_bank'),
    path('update/bank/<int:pk>/', views.UpdateBank.as_view(), name='update_bank'),
    path('delete/bank/<int:pk>/', views.DeletBank.as_view(), name='delete_bank'),
]