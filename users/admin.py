from django.contrib import admin

from users.models import User, EgeResults, Favorite, Feedback

admin.site.register(User)
admin.site.register(EgeResults)
admin.site.register(Favorite)
admin.site.register(Feedback)
