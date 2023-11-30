from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

class LocalListCreateView(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class AmbienteListCreateView(generics.ListCreateAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class DispositivoListCreateView(generics.ListCreateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

@api_view(['POST'])
def ligar_desligar_dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(pk=dispositivo_id)

    # Verificar se o dispositivo está ativo e fazer as operações necessárias

    dispositivo.save()
    return Response({'status': 'success'})