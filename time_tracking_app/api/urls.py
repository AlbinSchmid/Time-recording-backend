from django.urls import path
from .views import TimeRecordListView, StaffNameListView, ProjectListView


urlpatterns = [
    path('time-records/', TimeRecordListView.as_view(), name='time-record-list'),
    path('staff-names/', StaffNameListView.as_view(), name='staff-name-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]