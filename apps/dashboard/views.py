from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.event.models import Event


@login_required
def index(request):
    items = Event.objects.filter(added_by=request.user)

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
        },
    )


