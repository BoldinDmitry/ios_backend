from django.contrib.auth import login
from rest_framework import viewsets, mixins, views, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from universities.serializers import EdProgramSerializer
from users.models import User, Feedback, EgeResults, Favorite
from users.serializers import UserSerializer, FeedbackSerializer, EgeResultsSerializer, FavoriteSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed and created
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []


class LoginView(views.APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        token = data.get('token', )

        user = get_object_or_404(User, token=token)

        if user is not None:
            if user.is_active:
                login(request, user)
                serializer = UserSerializer(user)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FeedbackViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = []

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class EgeResultsViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = []

    queryset = EgeResults.objects.all()
    serializer_class = EgeResultsSerializer


class FavoriteEdProgramsViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def create(self, request, *args, **kwargs):
        print("PK::: ", request.user.pk)
        ed_programs_ids = request.data["education_programs_ids"]

        for ed_program_id in ed_programs_ids:
            favorite = Favorite(
                user_id=request.user.pk,
                education_program_id=ed_program_id
            )
            favorite.save()

        return Response(status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        university_id = request.GET.get('university_id')

        if university_id:
            queryset = self.queryset.filter(user_id=request.user.pk, education_program__university_id=university_id)
        else:
            queryset = self.queryset.filter(user_id=request.user.pk)

        education_programs = []
        for favorite in queryset:
            education_programs.append(favorite.education_program)

        serializer = EdProgramSerializer(education_programs, many=True, context={"request": request})

        return Response(serializer.data)
