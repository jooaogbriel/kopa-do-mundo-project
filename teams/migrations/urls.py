from django.urls import path
from . import views

urlpatterns = [
    path('api/teams/', views.TeamView.as_view()),
    path('api/teams/<team_id>/', views.TeamViewId.as_view()),
]