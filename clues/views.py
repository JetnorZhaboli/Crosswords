import datetime

from django.shortcuts import render

from clues.models import Crossword


def get_daily_crosswords(request):
    today = datetime.date.today()

    crosswords = (
        Crossword
            .objects
            .select_related("publisher")
            .prefetch_related("clues")
            .filter(published_on=today)
            .all()
    )

    return render(request, "clues/daily_crosswords.html", context={
        "today": today,
        "crosswords": crosswords,
    })


def get_crossword_details(request, pk):
    crossword = (
        Crossword
            .objects
            .select_related("publisher")
            .prefetch_related("clues")
            .get(pk=pk)
    )
    return render(request, "clues/crossword_detail.html", context={
        "crossword": crossword
    })
