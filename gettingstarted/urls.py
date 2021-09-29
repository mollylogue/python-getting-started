from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import myapp.views



from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'folder', myapp.views.FolderView)
router.register(r'document', myapp.views.DocumentView)
router.register(r'topic', myapp.views.TopicView)

urlpatterns = [
    path('', include(router.urls)),
    path("", myapp.views.index, name="index"),
    path("db/", myapp.views.db, name="db"),
]
