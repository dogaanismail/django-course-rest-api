from django.urls import path, include
from django.contrib import admin
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Course Django API",
        default_version="v1",
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.APIOverview.as_view(), name="ApiOverview"),
    path('courses/', views.ListCoursesView.as_view(), name="ViewCourses"),
    path('courses/add/', views.AddCourseView.as_view(), name="AddCourse"),
    path('courses/<str:id>/update', views.UpdateCourseView.as_view(), name="UpdateCourse"),
    path('courses/<str:id>/delete', views.DeleteCourseView.as_view(), name="DeleteCourse"),

    # Paths for Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
