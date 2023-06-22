from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='courier-home'),
    path('pages/track/', views.tracker, name='courier-track'),
    path('pages/tracking/', views.tracking, name='track-page'),
    path('pages/about/', views.about, name='about-page'),
    path('pages/contact/', views.feedback, name='contact'),
    path('pages/feed_success/', views.feedsuccess, name='success'),
]