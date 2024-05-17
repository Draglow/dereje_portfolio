from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="main_home" ),
    path ('contact/',views.contact_view, name='contact'),
    path('upload-cv/', views.upload_cv, name='upload_cv'),
    
    path('download-cv/', views.download_cv, name='download_cv'),


]