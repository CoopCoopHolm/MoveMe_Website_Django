from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('', views.index),
    path('consent', views.consent),
    path('moving', views.moving),
    path('junk_removal', views.junk_removal),
    path('consignment', views.consignment),
    path('quote/moving', views.quoteMoving),
    path('quote/junk_removal', views.quoteJunk_removal),
    path('quote/consignment', views.quoteConsignment),
    path('moving/review/<int:quote_id>', views.movingQuoteReview),
    path('junk_removal/review/<int:quote_id>', views.junk_removalQuoteReview),
    path('consignment/review/<int:quote_id>', views.consignmentQuoteReview),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )