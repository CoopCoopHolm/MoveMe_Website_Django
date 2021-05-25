from django.urls import path
from . import views



urlpatterns = [

    path('', views.index),
    path('consent', views.consent),
    path('moving', views.moving),
    path('junk_removal', views.junk_removal),
    path('consignment', views.consignment),
    path('consignment/', views.image_upload_view)
]
