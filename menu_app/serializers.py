from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from menu_app.views import custom_404, custom_401

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('menu_app.urls')),
]

handler404 = 'menu_app.views.custom_404'
handler500 = 'menu_app.middleware.CustomExceptionMiddleware.process_exception'