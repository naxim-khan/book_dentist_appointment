from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='home'),
    path('about_us',views.about_us, name='AboutUs'),
    path('appointment',views.appointment, name='appointment'),
    path('services',views.services, name='services'),
    path('team',views.team,name="team"),
    path('contact',views.contact,name="contact"),
    path('testimonials',views.testimonials, name="testimonials"),
    path('features',views.features, name='features'),
    path('dentist_registration',views.dentist_registration, name="register_dentist"),
    path('login',views.login_page, name='login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

