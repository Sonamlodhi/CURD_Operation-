from django.urls import path
from . import views

urlpatterns = [
    path('add_show/', views.add_show, name='addshow'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
]