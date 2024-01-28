from django.urls import path, include
from profile_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name='hello-viewset')
router.register('profile', views.UserProfileViewset)

urlpatterns = [
path('hello-view/',views.HelloApiView.as_view()),
path('', include(router.urls))
]
