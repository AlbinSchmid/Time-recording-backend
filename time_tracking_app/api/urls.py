from django.urls import path
from .views import TimeRecordListView, StaffNameListView, ProjectListView, TimeRecordDetailView


urlpatterns = [
    path('time-records/', TimeRecordListView.as_view(), name='time-record-list'),
    path('time-record/<int:pk>/', TimeRecordDetailView.as_view(), name='time-record-detail'),
    path('staff-names/', StaffNameListView.as_view(), name='staff-name-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]