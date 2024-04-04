from django.urls import path
from apps.settings import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("gallery/", views.gallery, name='gallery'),
    path("news/", views.news, name='news'),
    path("post/", views.post, name='post'),
    path("team/", views.team, name='team'),
]