from .models import User, EgeResults, Feedback
from rest_framework import serializers


class EgeResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgeResults
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)

        super().__init__(*args, **kwargs)
        if not remove_fields:
            return

        for field_name in remove_fields:
            self.fields.pop(field_name)

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(
        write_only=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    token = serializers.CharField(write_only=True, allow_blank=True)
    ege_results = EgeResultsSerializer(default=EgeResults.objects.create())

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "token",
            "first_name",
            "last_name",
            "date_joined",
            "ege_results",
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = '__all__'
