from django.urls import path
from . import views

urlpatterns = [
    path('workout_list_create/', views.WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workout_retrieve_update_destroy/<int:pk>/', views.WorkoutDetailView.as_view(),
         name='workout-retrieve-update-destroy'),
    path('exercises_list_create/', views.ExercisesListCreateView.as_view(), name='exercises-list-create'),
    path('exercises_retrieve_update_destroy/<int:pk>/', views.ExercisesDetailView.as_view(),
         name='exercises-retrieve-update-destroy'),
    path('measurements_list_create/', views.MeasurementsListCreateView.as_view(), name='measurements-list-create'),
    path('measurements_retrieve_update_destroy/<int:pk>/', views.MeasurementsDetailView.as_view(),
         name='measurements-retrieve-update-destroy'),
]
