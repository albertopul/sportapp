from rest_framework import serializers
from athletes.models import Athlete, Sponsor
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['username', 'user']


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    club = ProfileSerializer(many=False)
    class Meta:
        model = Athlete
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['username', 'user']