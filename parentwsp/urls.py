from django.urls import include, path

from . import views

session_urlpatterns = [
    path("", views.SessionCreateView.as_view(), name="session_create"),
]

urlpatterns = [
    path("", views.SessionListView.as_view(), name="home"),
    path("session/", include(session_urlpatterns)),
]
