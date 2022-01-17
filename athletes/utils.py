from .models import Athlete, Sponsor
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateAthletes(request, athletes, results):

    page = request.GET.get('page')
    paginator = Paginator(athletes, results)
    try:
        athletes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        athletes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        athletes = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, athletes

def searchAthletes(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    

    athletes = Athlete.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(club__name__icontains=search_query)
    )

    return athletes, search_query
