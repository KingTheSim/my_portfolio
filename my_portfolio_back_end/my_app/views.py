from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .serializers import ProjectSerializer
from .models import Project


class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self) -> QuerySet:
        language = self.request.query_params.get("language", None)
        if language:
            return Project.objects.filter(language=language)
        else:
            return Project.objects.all()


class ProjectDataView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
