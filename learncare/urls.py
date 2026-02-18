from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about/', views.aboutus, name='about'),
    path('colleges-and-courses/', views.colleges_nd_courses, name='college'),
    path('collage/details/<slug:slug>/',views.college_details,name="college_details"),
    path('contact/', views.contactus, name='contact'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)