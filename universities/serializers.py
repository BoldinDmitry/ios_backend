from rest_framework import serializers

from universities.models import University, UniversityPhotos, EdProgram


class EdProgramSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    university_id = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    def get_university_id(self, obj:  EdProgram):
        return obj.university.pk

    def get_university(self, obj:  EdProgram):
        return obj.university.name

    def get_photo(self, obj: EdProgram):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url)

    class Meta:
        model = EdProgram
        fields = [
            'id',
            'code',
            'name',
            'university',
            'university_id',
            'photo',
            'probability',
            'probability_number',
        ]


class UniversitySerializer(serializers.ModelSerializer):
    # photos = serializers.SerializerMethodField('get_photos', read_only=True)
    ed_programs = serializers.SerializerMethodField('get_ed_programs', read_only=True)

    # @staticmethod
    # def get_photos(university):
    #     photos = university.get_photos()
    #     return UniversityPhotosSerializer(photos, many=True).data

    @staticmethod
    def get_ed_programs(university):
        ed_programs = university.get_ed_programs()
        return EdProgramSerializer(ed_programs, many=True).data

    class Meta:
        model = University
        fields = ['id',
                  # 'photos',
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
