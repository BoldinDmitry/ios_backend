from django.shortcuts import render
from rest_framework import mixins, viewsets, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from universities.models import University
from universities.serializers import UniversitySerializer, EdProgramSerializer


class UniversitiesViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    authentication_classes = []


class EdProgramsView(views.APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        university_id = kwargs.get("university_id")
        if university_id is None:
            err_msg = {"error": "university_id id is required"}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=err_msg)

        university = get_object_or_404(University, id=university_id)

        ed_programs = university.get_ed_programs()
        ed_programs_serializer = EdProgramSerializer(ed_programs, many=True).data

        return Response(status=status.HTTP_200_OK, data=ed_programs_serializer)
