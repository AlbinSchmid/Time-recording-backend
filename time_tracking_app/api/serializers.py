from rest_framework import serializers
from time_tracking_app.models import TimeRecord, StaffName, Project

class TimeRecordSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = StaffName
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
