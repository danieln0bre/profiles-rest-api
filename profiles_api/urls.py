from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter() # Create a router object
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset') # Register the viewset with the router

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), # Add the hello-view/ path to the list of urlpatterns
    path('', include(router.urls)), # Add the router.urls path to the list of urlpatterns
]
