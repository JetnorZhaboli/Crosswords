from django.urls import path

from core import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact-us/", views.ContactView.as_view(), name="contact_us"),
    path("privacy-policy/", views.PrivacyView.as_view(), name="privacy_policy"),
]
