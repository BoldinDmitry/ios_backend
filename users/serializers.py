from .models import User, EgeResults, Feedback, Achievements
from rest_framework import serializers


class EgeResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgeResults
        fields = '__all__'


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
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
    token = serializers.CharField(allow_blank=True, read_only=True)
    ege_results = EgeResultsSerializer(required=False)
    achievements = AchievementsSerializer(required=False)

    def update(self, instance: User, validated_data):
        if self.validated_data.get('ege_results'):
            ege_results = self.validated_data.pop('ege_results')
            EgeResults.objects.update(**ege_results)

        if self.validated_data.get('achievements'):
            achievements = self.validated_data.pop('achievements')
            Achievements.objects.update(**achievements)

        super().update(instance, validated_data)

    def create(self, validated_data):
        if not validated_data.get("ege_results"):
            validated_data["ege_results"] = EgeResults.objects.create()
        if not validated_data.get("achievements"):
            validated_data["achievements"] = Achievements.objects.create()

        obj = User.objects.create(**validated_data)
        return obj

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
            "achievements"
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = '__all__'
