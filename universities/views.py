from typing import List

from rest_framework import mixins, viewsets, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from universities.models import University, EdProgram, UniversityPhotos
from universities.serializers import UniversitySerializer, EdProgramSerializer


class UniversitiesViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    pagination_class = None
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    authentication_classes = []


class EdProgramsViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pagination_class = None
    queryset = EdProgram.objects.all()
    serializer_class = EdProgramSerializer
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
        ed_programs_serializer = EdProgramSerializer(ed_programs, many=True, context={"request": request}).data

        return Response(status=status.HTTP_200_OK, data=ed_programs_serializer)


class UniversityPhotosView(views.APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        university_id = kwargs.get("university_id")
        if university_id is None:
            err_msg = {"error": "university_id id is required"}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=err_msg)

        university = get_object_or_404(University, id=university_id)

        photos: List[UniversityPhotos] = university.get_photos()
        photos_urls = []
        for photo in photos:
            # Todo rewrite this
            photos_urls.append("http://77.223.97.172:8081/"+photo.photo.url)

        return Response(status=status.HTTP_200_OK, data=photos_urls)
