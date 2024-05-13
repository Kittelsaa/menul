from django.urls import path
from .views import MenuItemListCreate, MenuItemDetail

urlpatterns = [
    path('menuitems/', MenuItemListCreate.as_view(), name='menuitem-list'),
    path('menuitems/<int:pk>/', MenuItemDetail.as_view(), name='menuitem-detail'),
]