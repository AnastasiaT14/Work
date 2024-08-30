from django.urls import path
from . import views

urlpatterns = [
    path('application_list_create/', views.ApplicationListCreateView.as_view(), name='application-list-create'),
    path('application_retrieve_update_destroy/<int:pk>/', views.ApplicationDetailView.as_view(),
         name='application-retrieve-update-destroy'),
    path('measurements_list_create/', views.MeasurementsListCreateView.as_view(), name='measurements-list-create'),
    path('measurements_retrieve_update_destroy/<int:pk>/', views.MeasurementsDetailView.as_view(),
         name='measurements-retrieve-update-destroy'),
]
