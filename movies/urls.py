from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shelf/add/', views.add_to_shelf, name='add_to_shelf'),
    path('my-shelf/', views.my_shelf, name='my_shelf'),
    path('remove/<int:movie_id>/', views.remove_movie, name='remove_movie'),
    path('status/<int:movie_id>/<str:new_status>/', views.change_status, name='change_status'),

    # ✅ New routes for thumbs up / down
    path('thumb-up/<int:movie_id>/', views.thumb_up, name='thumb_up'),
    path('thumb-down/<int:movie_id>/', views.thumb_down, name='thumb_down'),
]
