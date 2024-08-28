from django.urls import re_path
from .views import EmployeeViewSet, PerformanceReviewViewSet
from rest_framework import generics, mixins

urlpatterns = [
    # Employee routes
    re_path(r'^employees/create/?$', EmployeeViewSet.as_view({'post': 'create_employee'}), name='employee-create'),
    re_path(r'^employees/(?P<identifier>\w+)/?$', EmployeeViewSet.as_view({'get': 'retrieve_employee'}), name='employee-retrieve'),
    re_path(r'^employees/?$', EmployeeViewSet.as_view({'get': 'list'}), name='employee-list'),
    re_path(r'^employees/(?P<identifier>\w+)/update/?$', EmployeeViewSet.as_view({'put': 'update_employee', 'patch': 'update_employee'}), name='employee-update'),
    re_path(r'^employees/delete/(?P<identifier>\w+)/?$', EmployeeViewSet.as_view({'delete': 'delete_employee'}), name='employee-delete'),

    # Review routes
    # Review routes
    re_path(r'^employees/reviews/(?P<pk>\d+)/?$', PerformanceReviewViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='review-detail'),
    re_path(r'^employees/reviews/?$', PerformanceReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list'),
]