from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from detektor_suhu.models import Stats

class StatsViewset(viewsets.Modelviewsets):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer