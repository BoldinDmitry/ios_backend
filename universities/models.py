from django.db import models


class University(models.Model):
    name = models.TextField()
    about = models.TextField()
    site = models.TextField()
    preview = models.ImageField()
    qs = models.TextField()
    programs_counter = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()

    def get_photos(self):
        return UniversityPhotos.objects.filter(university=self)

    def get_ed_programs(self):
        return EdProgram.objects.filter(university=self)

    def __str__(self):
        return self.name


class UniversityPhotos(models.Model):
    photo = models.ImageField()
    description = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.university.name}: {self.description}"


class EdProgram(models.Model):
    code = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    photo = models.ImageField()
    probability = models.TextField()
    probability_number = models.FloatField()

    def __str__(self):
        return f"{self.university.name}: {self.code}"
