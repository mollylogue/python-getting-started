from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from myapp.models import Folder, Document, Topic
from myapp.serializers import FolderSerializer, DocumentSerializer, TopicSerializer
import json

from .views import index


class FolderEndpointTest(TestCase):

    def setUp(self):
        self.client = Client()
        Folder.objects.create(name="My Test Folder")

    def test_get_folders(self):
        response = self.client.get('/folder/')
        expected = Folder.objects.all()
        expected_serialized = FolderSerializer(expected, many=True)
        self.assertEqual(response.data, expected_serialized.data)

    def test_create_new_folder(self):
        request_payload = {
            'name': 'test create new folder'
        }
        response = self.client.post('/folder/',
            data=json.dumps(request_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_folder(self):
        request_payload = {
            'bad_field': "asdf"
        }
        response = self.client.post('/folder/',
            data=json.dumps(request_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DocumentEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = APIRequestFactory()
        test_folder = Folder.objects.create(name="Test Folder")
        Document.objects.create(name="my_test_document", folder=test_folder)

    def test_get_documents(self):
        request = self.factory.get('/document/')
        serializer_context = {
            'request': request,
        }

        response = self.client.get('/document/')
        expected = Document.objects.all()
        expected_serialized = DocumentSerializer(expected, many=True, context=serializer_context)
        self.assertEqual(response.data, expected_serialized.data)
