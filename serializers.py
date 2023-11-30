from rest_framework import serializers

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'
