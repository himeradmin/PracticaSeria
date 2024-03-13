from rest_framework import serializers
from app1.models import Empleo
from app1.serializers import PersonalSerializers


class EmpleoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleo
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "nombre": instance.nombre,
            "persona_empleo":instance.persona_empleo.nombre,
            "aspiracion":instance.aspiracion,
            "experiencia":instance.experiencia
        }