from rest_framework import serializers
from .models import  Personal

class PersonalSerializers(serializers.ModelSerializer):
    class Meta:
        model= Personal
        exclude= ("id",)

    def validate_nombre(self,value):
        if "H".lower() not in value:
            raise  serializers.ValidationError("Tiene que tener una 'H'")
        return value

    def validate_edad(self,value):
        if value >18 and value <30:
            raise serializers.ValidationError("Tienes que ser mayor de 18 y menor que 30")
        return value

