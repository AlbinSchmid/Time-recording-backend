from rest_framework import generics
from time_tracking_app.models import TimeRecord, StaffName, Project
from .serializers import TimeRecordSerializer, StaffNameSerializer, ProjectSerializer

class TimeRecordListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create time records.
    """
    queryset = TimeRecord.objects.all()
    serializer_class = TimeRecordSerializer


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