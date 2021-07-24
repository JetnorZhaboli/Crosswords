from django.urls import path

from clues import views


urlpatterns = [
    path("daily-crosswords/", views.get_daily_crosswords, name="daily_crosswords"),
    path("crosswords/<int:pk>/", views.get_crossword_details, name="crossword_detail"),
]
