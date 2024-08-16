from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name="webhome"),
 #   path('about/', views.About, name="About"),
  #  path('1/', views.F, name="1"),
   # path('movies/<int:movie_id>', views.movie),
    path('', views.HomeBase, name="webHomeBase"),
    path('ContactBase', views.ContactBase, name="webContactBase"),
    path('AboutUsBase', views.AboutUsBase, name="webAboutUsBase"),
    path('BookingBase', views.BookingBase, name="webBookingBase"),
  #  path('MenuT', views.MenuT, name="webMenuT"),
    path('AddToCartT', views.AddToCartT, name="webAddToCartT"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)