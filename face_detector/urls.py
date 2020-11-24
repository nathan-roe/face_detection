from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('detect_face', views.detect_face),
    path('process_login', views.process_login),
    path('process_reg', views.process_reg),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('edit_page', views.edit_page)


]