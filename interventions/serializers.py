from rest_framework import serializers
from .models import Intervention

class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = ('intervention_title', 'intervention_type', 'intervention_status', 'intervention_date', 'address', 'city', 'state')

class InterventionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'
        lookup_field = 'intervention_title'