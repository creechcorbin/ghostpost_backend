from rest_framework import serializers
from api.models import Boast, Roast

class BoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boast
        fields = [
            'content',
            'up_votes',
            'down_votes',
            'post_time',
        ]

class RoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roast
        fields = [
            'content',
            'up_votes',
            'down_votes',
            'post_time',
        ]