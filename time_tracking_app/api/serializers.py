from rest_framework import serializers
from time_tracking_app.models import TimeRecord, StaffName, Project

class TimeRecordSerializer(serializers.ModelSerializer):
    """Serializer for TimeRecord model, including related fields for staff and project names."""
    staff_name = serializers.StringRelatedField()
    project_name = serializers.StringRelatedField()
    staff_id = serializers.PrimaryKeyRelatedField(
        queryset=StaffName.objects.all(),
        write_only=True,
        source='staff_name'
    )
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        write_only=True,
        source='project_name'
    )

    class Meta:
        model = TimeRecord
        fields = '__all__'


class StaffNameSerializer(serializers.ModelSerializer):
    """Serializer for StaffName model."""
    class Meta:
        model = StaffName
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""
    class Meta:
        model = Project
        fields = '__all__'
