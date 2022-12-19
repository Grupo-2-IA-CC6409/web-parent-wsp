from django.urls import include, path

from . import views

session_api_urlpatterns = [
    path("notification/", views.SessionNotificationAPI.as_view()),
    path("disconnect/", views.SessionDisconnectAPI.as_view()),
]

session_urlpatterns = [
    path("create/", views.SessionCreateView.as_view(), name="session_create"),
    path("<int:pk>/delete/", views.SessionDeleteView.as_view(), name="session_delete"),
    path("<int:pk>/update/", views.SessionUpdateView.as_view(), name="session_update"),
    path(
        "<int:pk>/notifications/",
        views.SessionNotificationView.as_view(),
        name="session_notifications",
    ),
    path("api/", include(session_api_urlpatterns)),
]

urlpatterns = [
    path("", views.SessionListView.as_view(), name="home"),
    path("session/", include(session_urlpatterns)),
]
