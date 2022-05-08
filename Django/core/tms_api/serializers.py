from rest_framework import serializers
from tms.models import Request


class RequestSerializer(serializers.ModelSerializer):
    partial_day_display = serializers.ReadOnlyField(
        source='get_partial_day_display')

    class Meta:
        model = Request
        fields = ('id', 'owner', 'owner_name', 'request_type', 'request_type_name',
                  'start_date', 'end_date', 'partial_day', 'partial_day_display', 'duration',
                  'reason', 'reason_name', 'approver', 'approver_name',
                  'detail_reason', 'supervisor', 'supervisor_name',
                  'inform_to', 'inform_to_name', 'expected_approve', 'time')
        read_only_fields = ('id', 'owner', 'owner_name', 'partial_day_display', 'duration',
                            'request_type_name', 'reason_name', 'approver_name',
                            'supervisor_name', 'inform_to_name')
