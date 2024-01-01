from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer


class APIOverview(generics.GenericAPIView):
    def get(self, request):
        api_urls = {
            'To Return all Courses': '/courses',
            'To add a new Course': '/courses/add',
            'Update a Course': '/courses/{CourseId}/update',
            'Delete a Course': '/courses/{CourseId}/delete',
        }
        return Response(api_urls, status=status.HTTP_200_OK)


class ListCoursesView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AddCourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class UpdateCourseView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Course.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.kwargs.get(self.lookup_field))
        return obj


class DeleteCourseView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'
