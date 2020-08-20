from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("edit/<int:task_id>", views.edit, name="edit"),
    path("complete/<int:task_id>", views.complete, name="complete"),
    path("sprint/<int:task_id>", views.sprint, name="sprint"),
    path("sprint", views.standalone_sprint, name="sprint"),
    path("download/<str:file_url>", views.download_file, name="download"),
]