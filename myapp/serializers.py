from .models import Folder, Document, Topic
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'folders', 'documents']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'name', 'link', 'folder', 'created_at', 'updated_at', 'topic']

class FolderSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Folder
        fields = ['id', 'name', 'topic', 'created_at', 'updated_at', 'documents']
