from rest_framework import serializers
from empresa.models import Alvos


# Register your serializers here.
class AlvosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alvos
        fields = "__all__"
