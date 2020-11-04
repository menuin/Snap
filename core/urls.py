from django.conf import settings
from django.urls import path
from core import views
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('movingin/',views.moving_in,name='moving_in'),
    path('<int:pk>/snap/',views.snap,name='snap'),
    path('<int:pk>/detail',views.love_love,name='love_love'),
    path('<int:pk>/detail',views.couple_main,name='couple_main'),
    path('<int:pk>/movingout',views.moving_out,name='moving_out'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)