from rest_framework import serializers
from posts import models


class postserializers(serializers.ModelSerializer):
    class meta :
        model = models.post
        fields = ("posted_by_id", "message")