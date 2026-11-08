from django.urls import path,include
from rest_framework.routers import DefaultRouter
from movie.views import MovieView

router=DefaultRouter()
router.register(r'movie',MovieView,basename="movie")

urlpatterns = [
    path('',include(router.urls))
]
