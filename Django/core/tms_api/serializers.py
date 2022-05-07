from dataclasses import field
from rest_framework import serializers
from tms.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('owner', 'request_type', 'start_date', 'end_date', 'partial_day', 'reason',
                  'approver', 'detail_reason', 'supervisor', 'inform_to', 'expected_approve', 'time')
