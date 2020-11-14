from rest_framework import serializers

from universities.models import University, UniversityPhotos, EdProgram


class UniversitySerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos', read_only=True)

    @staticmethod
    def get_photos(university):
        photos = university.get_photos()
        return UniversityPhotosSerializer(photos, many=True).data

    class Meta:
        model = University
        fields = '__all__'


class UniversityPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityPhotos
        fields = '__all__'


class EdProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdProgram
        fields = '__all__'
