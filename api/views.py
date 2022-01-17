from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import AthleteSerializer, ClubSerializer
from athletes.models import Athlete, Sponsor
from users.models import Profile


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'api/athletes'},
        {'GET':'api/athletes/id'},

        {'GET':'api/clubs'},
        {'GET':'api/clubs/id'},
        
    ]
    return Response(routes)


@api_view(['GET'])
def getAthletes(request):
    athletes = Athlete.objects.all()
    serializer = AthleteSerializer(athletes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAthlete(request, pk):
    athlete = Athlete.objects.get(id=pk)
    serializer = AthleteSerializer(athlete, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getClubs(request):
    clubs = Profile.objects.all()
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getClub(request, pk):
    club = Profile.objects.get(id=pk)
    serializer = ClubSerializer(club, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeSponsor(request):
    sponsorId = request.data['sponsor']
    athleteId = request.data['athlete']

    athlete = Athlete.objects.get(id=athleteId)
    sponsor = Sponsor.objects.get(id=sponsorId)

    athlete.sponsors.remove(sponsor)

    return Response('Sponsor was deleted!')