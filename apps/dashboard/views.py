from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(added_by=request.user)

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
        },
    )


