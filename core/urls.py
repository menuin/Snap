from django.conf import settings
from django.urls import path
from core import views
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('movingin/',views.moving_in,name='moving_in'),
    path('bangal/',views.반갈죽,name='bangal'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)