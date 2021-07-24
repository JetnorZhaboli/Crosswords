from django.urls import path

from clues import views


urlpatterns = [
    path("daily-crosswords/", views.get_daily_crosswords, name="daily_crosswords"),
    path("crosswords/<int:pk>/", views.get_crossword_details, name="crossword_detail"),
    path("publishers/", views.PublisherListView.as_view(), name="publisher_list"),
    path("publishers/<slug>/", views.PublisherDetailView.as_view(), name="publisher_detail"),
    path("clues/<slug>/", views.ClueDetailView.as_view(), name="clue_detail"),
]
