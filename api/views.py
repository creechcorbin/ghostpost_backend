from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, routers
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import BoastSerializer, RoastSerializer
from api.models import Boast, Roast
from drf_multiple_model.views import ObjectMultipleModelAPIView


class HomeAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Boast.objects.order_by('-post_time'), 'serializer_class': BoastSerializer},
        {'queryset': Roast.objects.order_by('-post_time'), 'serializer_class': RoastSerializer},
    ]


class BoastViewSet(viewsets.ModelViewSet):
    queryset = Boast.objects.all()
    serializer_class = BoastSerializer

    @action(detail=True, methods=['post'])
    def up_vote_boast(self, request, pk=None):
        boast = self.get_object()
        serializer = BoastSerializer(data=request.data)
        if serializer.is_valid():
            boast.up_votes += 1
            boast.save()
            return Response({'status': 'boast upvoted'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def down_vote_boast(self, request, pk=None):
        boast = self.get_object()
        serializer = BoastSerializer(data=request.data)
        if serializer.is_valid():
            boast.down_votes += 1
            boast.save()
            return Response({'status': 'boast downvoted'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class RoastViewSet(viewsets.ModelViewSet):
    queryset = Roast.objects.all()
    serializer_class = RoastSerializer

    @action(detail=True, methods=['post'])
    def up_vote_roast(self, request, pk=None):
        roast = self.get_object()
        serializer = RoastSerializer(data=request.data)
        if serializer.is_valid():
            roast.up_vote += 1
            roast.save()
            return Response({'status': 'roast upvoted'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def down_vote_roast(self, request, pk=None):
        roast = self.get_object()
        serializer = RoastSerializer
        if serializer.is_valid():
            roast.down_vote += 1
            roast.save()
            return Response({'status': 'roast downvoted'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
