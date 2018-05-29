from rest_framework import serializers
from evaluations.models import Evaluation


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('user', 'comment', 'record', 'date')
