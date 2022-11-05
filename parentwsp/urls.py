from django.urls import include, path

from . import views

session_urlpatterns = [
    path("create/", views.SessionCreateView.as_view(), name="session_create"),
    path("<int:pk>/delete/", views.SessionDeleteView.as_view(), name="session_delete"),
    path("<int:pk>/update/", views.SessionUpdateView.as_view(), name="session_update"),
]

urlpatterns = [
    path("", views.SessionListView.as_view(), name="home"),
    path("session/", include(session_urlpatterns)),
]
