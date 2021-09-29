from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Greeting, Folder, Document, Topic
from .serializers import FolderSerializer, DocumentSerializer, TopicSerializer

class FolderView(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

class TopicView(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

# Create your views here.
def index(request):
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
