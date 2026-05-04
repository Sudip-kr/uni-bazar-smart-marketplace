from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.create_item, name='create_item'),
    path('my-items/', views.my_items, name='my_items'),
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('<int:pk>/mark-sold/', views.mark_as_sold, name='mark_as_sold'),
    path('<int:pk>/wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
     path('<int:pk>/', views.item_detail, name='item_detail'),
     path('wishlist/', views.wishlist_items, name='wishlist_items'),
]