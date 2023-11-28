from django.urls import path
from .views import ProjectListCreateView, ProjectDataView

urlpatterns = [
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("projects/<int:pk>", ProjectDataView.as_view(), name="project-details")
]