from rest_framework import serializers

from universities.models import University, UniversityPhotos, EdProgram


class EdProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdProgram
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos', read_only=True)
    ed_programs = serializers.SerializerMethodField('get_ed_programs', read_only=True)

    @staticmethod
    def get_photos(university):
        photos = university.get_photos()
        return UniversityPhotosSerializer(photos, many=True).data

    @staticmethod
    def get_ed_programs(university):
        ed_programs = university.get_ed_programs()
        return EdProgramSerializer(ed_programs, many=True).data

    class Meta:
        model = University
        fields = ['id',
                  'photos',
                  'ed_programs',
                  'name',
                  'about',
                  'site',
                  'preview',
                  'qs',
                  'programs_counter',
                  'lat',
                  'lon']


class UniversityPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityPhotos
        fields = '__all__'
