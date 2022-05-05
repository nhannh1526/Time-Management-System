from rest_framework import serializers
from tms.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_on', 'slug']
        model = Request
