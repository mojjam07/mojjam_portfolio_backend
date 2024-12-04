from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectListView,
    ConsultViewSet,
    QuestionViewSet,
    TestimonialListView,
    ContactListView
)

router = DefaultRouter()
router.register(r'consults', ConsultViewSet, basename='consult')
router.register(r'questions', QuestionViewSet, basename='question')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/testimonials/', TestimonialListView.as_view(), name='testimonials'),
    path('api/contacts/', ContactListView.as_view(), name='contacts'),
    path('api/projects/', ProjectListView.as_view(), name='project'),
]
