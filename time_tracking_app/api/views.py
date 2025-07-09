from rest_framework import generics
from time_tracking_app.models import TimeRecord, StaffName, Project
from .serializers import TimeRecordSerializer, StaffNameSerializer, ProjectSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class TimeRecordListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create time records.
    """
    queryset = TimeRecord.objects.all()
    serializer_class = TimeRecordSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['staff_name']
    search_fields = ['staff_name__id']
    

class TimeRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific time record.
    """
    queryset = TimeRecord.objects.all()
    serializer_class = TimeRecordSerializer
    lookup_field = 'pk'


class StaffNameListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create staff names.
    """
    queryset = StaffName.objects.all()
    serializer_class = StaffNameSerializer


class ProjectListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer