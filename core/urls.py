from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    api_root, RegisterView, UserView,
    StudentViewSet, TeacherViewSet, CourseViewSet,
    SubjectViewSet, AttendanceViewSet, ExamViewSet,
    ResultViewSet, FeeViewSet, TimetableViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'results', ResultViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'timetable', TimetableViewSet)

urlpatterns = [
    path("api/", api_root, name="api_root"),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/me/", UserView.as_view(), name="profile"),
    path("api/v1/", include(router.urls)),  # CRUD endpoints
]
