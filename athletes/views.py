from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Athlete, Sponsor
from .forms import AthleteForm
from .utils import searchAthletes, paginateAthletes

def athletes(request):

    athletes, search_query = searchAthletes(request)
    custom_range, athletes = paginateAthletes(request, athletes, 3)
    

    context = {'athletes':athletes, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'athletes/athletes.html', context)


def athlete(request, pk):
    athleteObj = Athlete.objects.get(id=pk)
    return render(request, 'athletes/single-athlete.html', {'athlete':athleteObj})

@login_required(login_url="login")
def createAthlete(request):
    profile = request.user.profile
    form = AthleteForm()

    if request.method == 'POST':
        sponsors = request.POST.get('sponsors').split(',')
        form = AthleteForm(request.POST, request.FILES)
        if form.is_valid():
            athlete = form.save(commit=False)
            athlete.club = profile
            athlete.save()
            
            for sponsor in athlete.sponsors.all():
                sponsor, created = Sponsor.objects.get_or_create(name=sponsor)
                athlete.sponsors.add(sponsor)
            return redirect('account')

    context = {'form': form}
    return render(request, "athletes/athlete_form.html", context)

@login_required(login_url="login")
def updateAthlete(request, pk):
    profile = request.user.profile
    athlete = profile.athlete_set.get(id=pk)
    form = AthleteForm(instance=athlete)

    if request.method == 'POST':
        sponsors = request.POST.get('sponsors').split(',')
        form = AthleteForm(request.POST, request.FILES, instance=athlete)
        if form.is_valid():
            form.save()
            for sponsor in sponsors:
                sponsor, created = Sponsor.objects.get_or_create(name=sponsor)
                athlete.sponsors.add(sponsor)
            return redirect('account')

    context = {'form': form, 'athlete': athlete}
    return render(request, "athletes/athlete_form.html", context)

@login_required(login_url="login")
def deleteAthlete(request, pk):
    profile = request.user.profile
    athlete = profile.athlete_set.get(id=pk)
    if request.method == 'POST':
        athlete.delete()
        return redirect('account')
    context = {'object': athlete}
    return render(request, 'delete-template.html', context)

