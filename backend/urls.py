"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static

from backend import settings
from users import views as users_views
from universities import views as universities_views

router = routers.SimpleRouter()

router.register(r"users/education_programs", users_views.FavoriteEdProgramsViewSet)
router.register(r"users", users_views.UserViewSet)
router.register(r"universities", universities_views.UniversitiesViewSet)
router.register(r"feedback", users_views.FeedbackViewSet)
router.register(r"ege_results", users_views.EgeResultsViewSet)
router.register(r"education_programs", universities_views.EdProgramsViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/login/", users_views.LoginView.as_view()),

    path("api/v1/universities/<int:university_id>/programs/", universities_views.EdProgramsView.as_view()),
    path("api/v1/universities/<int:university_id>/photos/", universities_views.UniversityPhotosView.as_view()),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
